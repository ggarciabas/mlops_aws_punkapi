import base64
import json

filter_keys = ['id', 'name', 'abv', 'ibu', 'target_fg', 'target_og', 'ebc', 'srm', 'ph']

def lambda_handler(event, context):
    output = []

    print (f"Leitura dos registros: {len(event['records'])}")
    for record in event['records']:
        print(f"ID: {record['recordId']}")
        payload = base64.b64decode(record['data'])

        # Recupera campos específicos para modelo
        print (f"Payload: {payload}")
        data_str = payload.decode()
        print (f"Data string: {data_str}")
        data_dict = json.loads(data_str)
        print (f"Data dict: {data_dict}")
        final_data  = { k: data_dict[k] for k in filter_keys }
        print (f"Chaves finais: {final_data.keys()}")
        encoded_data = f"{final_data}\n".encode()
        print (f"Encoded final data: {encoded_data}")

        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(encoded_data)
        }
        output.append(output_record)

    print(f"Processado {len(event['records'])} registros com sucesso.")

    return {'records': output}

# Ref: https://github.com/amazon-archives/serverless-app-examples/blob/master/python/kinesis-firehose-process-record-python/lambda_function.py