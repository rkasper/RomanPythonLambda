import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello Richard',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'event' : event,
        'roman' : event['queryStringParameters']['roman']
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
