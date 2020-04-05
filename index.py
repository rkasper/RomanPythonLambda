import json
import datetime

from roman import convert


def handler(event, context):
    """
    Roman Numerals converter - Amazon Lambda web service

    Just push to master, and the code will get pulled through the CodeStar build pipeline.

    To invoke the service, do an HTTPS GET https://blahblahblah.execute-api.us-east-2.amazonaws.com/Prod?roman=XXX
    where XXX is the Roman number to convert to Arabic.

    Examples:
        $ curl https://blahblahblah.execute-api.us-east-2.amazonaws.com/Prod?roman=I
        1
        $ curl https://blahblahblah.execute-api.us-east-2.amazonaws.com/Prod?roman=V
        5
    """
    roman = event['queryStringParameters']['roman']
    arabic = str(convert(roman))

    return {'statusCode': 200,
            'body': arabic,
            'headers': {'Content-Type': 'text/plain'}}
