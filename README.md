Roman Numerals kata in Python and Amazon Lambda
===============================================

This is a Roman Numerals converter implemented in Python. It runs on Amazon Lambda.

Just push to master, and the code will get pulled through the CodeStar build pipeline.

To invoke the service, do an HTTPS GET https://blahblahblah.execute-api.us-east-2.amazonaws.com/Prod?roman=XXX
where XXX is the Roman number to convert to Arabic.

Examples:
```
$ curl https://blahblahblah.execute-api.us-east-2.amazonaws.com/Prod?roman=I
1
$ curl https://blahblahblah.execute-api.us-east-2.amazonaws.com/Prod?roman=V
5
```
(Replace blahblahblah with your endpoint's hostname.)