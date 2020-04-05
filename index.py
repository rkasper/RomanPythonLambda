import json
import datetime


def handler(event, context):
    roman = event['queryStringParameters']['roman']
    if roman == 'I':
        arabic = '1'
    else:
        arabic = '5'

    return {'statusCode': 200,
            # 'body': json.dumps(data),
            'body': arabic,
            'headers': {'Content-Type': 'application/json'}}
