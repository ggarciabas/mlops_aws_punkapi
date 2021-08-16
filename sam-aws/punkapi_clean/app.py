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
        data_str = payload.decode(encoding='utf-8').replace("'", '"')
        data_dict = json.loads(data)
        final_data  = { k: data_dict[k] for k in filter_keys }
        print (f"Chaves finais: {final_data.keys()}")

        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(final_data)
        }
        output.append(output_record)

    print(f"Processado {len(event['records'])} registros com sucesso."))

    return {'records': output}

# Ref: https://github.com/amazon-archives/serverless-app-examples/blob/master/python/kinesis-firehose-process-record-python/lambda_function.py