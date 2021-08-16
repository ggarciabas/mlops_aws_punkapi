import base64
import json

def lambda_handler(event, context):
    output = []

    print (f"Leitura dos registros: {len(event['records'])}")
    for record in event['records']:
        print(record['recordId'])
        payload = base64.b64decode(record['data'])

        print (payload)
        try:
            print (type(payload)))
        except:
            print ("Falha type")

        try:
            json_dp = json.dump(payload)
            print (json_dp)
            print (type(json))
        except:
            print ("Falha json")

        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(payload)
        }
        output.append(output_record)

    print('Processado {} registros com sucesso.'.format(len(event['records'])))

    return {'records': output}

# Ref: https://github.com/amazon-archives/serverless-app-examples/blob/master/python/kinesis-firehose-process-record-python/lambda_function.py