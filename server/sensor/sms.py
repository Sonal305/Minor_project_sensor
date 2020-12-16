import http.client
from decouple import config
from django.http import HttpResponse
import requests

def send_sms(contact, message):
    print(contact, message, "called")

    url = "https://www.fast2sms.com/dev/bulk"
    querystring = {

        "authorization":"85oS0TyPFWwgdeHXQN2mE6l73vbYCJrkKVUOsLGxIjtufq4pBicNXekgl70K3WBaVLbzGr6jCI9UoSZT",
        "sender_id":"FSTSMS",
        "message":message,
        "language":"english",
        "route":"p",
        "numbers":str(contact)
    }

    headers = {
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)



#send_sms("7000253310", "It worked")
