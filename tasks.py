from microsoftbotframework import ReplyToActivity

import json
import urllib


def echo_response(message):
    account_key1 = '99cb1aae89694dc78c98534e3c0fc6ab'
    account_key2 = '10f71682c9fc4833a9a3243c3c832829'

    base_url1 = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'

    headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key2}
    sentiment_scores = []

    inputtxt2json = '{"documents":['

    inputtxt = '{"language":"en",'
    inputtxt = inputtxt + '"id":"1"'
    inputtxt = inputtxt + '"text":' + message

    inputtxt2json = inputtxt + ']}'

    req = urllib.Request(base_url1, inputtxt2json, headers)
    response = urllib.urlopen(req)

    result = response.read()
    obj = json.loads(result)

    for sentiment_analysis in obj['documents']:
        sentiment_scores.append(str(sentiment_analysis['score']))

    message1 = sentiment_scores

    if message["type"] == 'message1':
        ReplyToActivity(fill=message1, text=message1["text"]).send()

    # if message["type"] == 'message':
    #     ReplyToActivity(fill=message, text=message["text"]).send()
