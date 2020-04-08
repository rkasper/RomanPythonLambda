import logging

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

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logger.info('event is: ' + str(event))

    parameters = event['queryStringParameters']
    if parameters is None:
        logger.info('Received no arguments. Returning documentation.')
        body = 'I convert Roman numerals to Arabic integers. To invoke me, use the ?roman= parameter. For example: ' \
               '?roman="V" '
    else:
        roman = parameters['roman']
        logger.info('Received argument ?roman="' + roman)
        arabic = str(convert(roman))
        logger.info('Returning arabic ' + arabic)
        body = arabic

    return {'statusCode': 200,
            'body': body,
            'headers': {'Content-Type': 'text/plain'}}
