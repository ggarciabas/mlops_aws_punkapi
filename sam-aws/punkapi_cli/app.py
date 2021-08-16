"""
    Consome Punk API

    Função lambda para consumir o endpoint https://api.punkapi.com/v2/beers/random.
"""

import requests
import json
import boto3
import os
import sys

kinesis_stream = os.environ.get('KinesisStreamName')

def exception_handler(e):
    """
        Retorna erro

        Ref: https://stackoverflow.com/questions/60225185/how-to-throw-http-error-code-with-aws-lambda-using-lambda-proxy
    """
    status_code = 400
    return {
        'statusCode': status_code,
        'body': json.dumps(str(e))
    }

def lambda_handler (event, context):
    """
        Requisita endpoint com método GET para obter as bebidas aleatórias 
            e ingere informação no Kinesis Data Stream.

        Lambda logs: https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html#python-logging-output
        Kinesis putRecord: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html
    """

    print ("Requisita dados para PunkAPI")
    res = requests.get('https://api.punkapi.com/v2/beers/random')

    if res.status_code == requests.codes.ok:
        # Recupera dados da requisição
        res_json = res.json()
        print (f" JSON: {res_json[0]}")
        res_json_dumps = json.dumps(res_json[0]) # mantém aspas duplas
        print (f"JSON dumps: {res_json_dumps}")
        encoded_data = str(res_json_dumps).encode()
        print (f"Encoded data: {encoded_data}")
        print (f"Size: {sys.getsizeof(encoded_data)}")

        # Envia dados para Kinesis
        print (f"Envia dados para Kinesis Data Stream: {kinesis_stream}")
        client = boto3.client('kinesis')
        kinesis_resp = client.put_record(
                            StreamName=kinesis_stream,
                            Data=encoded_data,
                            PartitionKey='partitionKey-1'
                            )
        print(f"Kinesis resp: {kinesis_resp}")
    
    return None