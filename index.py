import json
import datetime

from roman import convert


def handler(event, context):
    roman = event['queryStringParameters']['roman']
    arabic = str(convert(roman))

    return {'statusCode': 200,
            'body': arabic,
            'headers': {'Content-Type': 'application/json'}}
