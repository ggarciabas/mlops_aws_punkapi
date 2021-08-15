"""
    Consome Punk API

    Função lambda para consumir o endpoint https://api.punkapi.com/v2/beers/random.
"""

import requests

def lambda_handler (event, context):
    """
        Requisita endpoint com método GET para obter as bebidas aleatórias.

        Lambda logs: https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html#python-logging-output
    """

    res = requests.get('https://api.punkapi.com/v2/beers/random')
    res_json = res.json()
    print (res_json[0])

    return True