# from email import message
import json
import string
from wsgiref import headers

import requests
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
from twilio.twiml.messaging_response import (Body, Message, MessagingResponse,
                                             Redirect)

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
last_jid = None
account_sid = 'ACc36e6423c66202ccdc767d631d226c79' 
auth_token = 'f3f6a62fdf344c566ec02cd330b28501'
client = Client(account_sid, auth_token)
#new_sentinel_id = None
auth="Token 527c4eac4d4afcd8e6625fc833ae67e4f83af6d69d2271df81de54fb788371ea"
sent="urn:uuid:22107c17-89d8-4e29-aaa6-f18b6a02f68e"


@csrf_exempt
def bot(request):
    global last_jid
    sender_message = request.POST["Body"],
    sender_number = request.POST["From"]
    last_jid = last_jid
    #new_sentinel_id = new_sentinel_id
    url = "http://0.0.0.0:9000/js/walker_run"
    #if (new_sentinel_id):sent = new_sentinel_id
    payload = json.dumps({
        "name": "talker",
        'nd': last_jid,
        "ctx": {
            "utterance": sender_message[0], 
            "phone_number":sender_number
            },
        "_req_ctx": {},
        "snt": sent,
        "profiling": False,
        "is_async": False
    })
    headers = {
    'Authorization': auth,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    #steriliser = StockSerializer(response, many = True)
    data = response.json()
    #data = requests.get(url,headers=headers).json()
    #print(data)
    print(last_jid)
    print(data["report"][0]["node"]["jid"])
    last_jid = data["report"][0]["node"]["jid"]
    #print(response.json()) 
    return HttpResponse(response)







    # headers = {
    #     'accept': 'application/json',
    #     'Authorization': auth,
    #     'Content-Type': 'application/json',
    # }

    # sender_mes_jac = {
    #     "name": "talker",
    #     "ctx": {"question": sender_message[0], "phone_number":sender_number},
    #     "_req_ctx": {},
    #     "snt": sent,
    #     "profiling": False,
    #     "is_async": False
    # }

    # response = requests.post("http://0.0.0.0:8000/js/walker_run", headers=headers, json=sender_mes_jac)
    # return HttpResponse(response)






    # messaged = client.messages \
    #             .create(
    #                  body="Hey {}, how are you?".format(sender_name[0]),
    #                  from_='whatsapp:+14155238886',
    #                  to=sender_number
    #              )

    # if request.method =='POST':
    #     messaged = client.messages \
    #             .create(
    #                  body="Hey {}, how are you?".format(sender_name[0]),
    #                  from_='whatsapp:+14155238886',
    #                  to=sender_number
    #              )
        # messaged
        # print(request.POST)

    # if sender_message[0] == "hi":
    #     messaged
        # sendm(sender_message)
        # print(request.POST)

    # ll = request.POST


    # return HttpResponse("hellos")





# def sendm(sender_message):

    # headers = {
    #     'accept': 'application/json',
    #     'Content-Type': 'application/json',
    # }


    # print(sender_message)
    # return sender_message
    

    # data = '{\n  "message_sent": "{fsd}"\n}'.format(fsd=sender_message[0])
    # data:string = "{{message_sent}: '{oo}'}".format(message_sent="message_sent",oo=sender_message[0])
    # mm = "data"d
    # data = {'message_sent': request.POST}
    # data = [{'message_sent': 'kkkkkk'}]
    # data = sender_message
    # print(sender_message)
    
    # message:dict ={ "message": {
    # "sender_message": sender_message,
    # "sender_name": sender_name
    # }}



    # data = json.loads("{\"key1\": 1, \"key2\": 2}")
    # data = json.loads("[\"string\", 1, 2.5, null]")
    # sender_mes_jac:dict = {
    #     name: "talker",
    #     ctx: {"sender_message": "sender_message[0]"},
    #     _req_ctx: {},
    #     snt: sent,
    #     profiling: False
    # }


    # json.stringify(message)
    # json.append("name": "talker",
    #     "ctx": {"sender_message": sender_message[0]},
    #     "_req_ctx": {},
    #     "snt": sent,
    #     "profiling": False)



    # response = requests.post('http://0.0.0.0:8005/twilio_bot/', headers=headers, data=json.dumps(message)
    # response = requests.post('http://0.0.0.0:8005/twilio_bot_receive/', headers=headers, data=json.dumps(message)
    # response = requests.post("http://0.0.0.0:8000/js/walker_run", headers=headers, json=json.dumps(sender_mes_jac))

    # response = requests.post("http://0.0.0.0:8000/js/walker_run", headers=headers, data=json.dumps(data))
    # response = requests.post("http://0.0.0.0:8000/js/walker_run", headers=headers, data=data)

    # return sender_message
    # http://0.0.0.0:8000/js/walker_run

    # return response

    # from twilio.twiml.messaging_response import Message, MessagingResponse

    # response = MessagingResponse()
    # response.message('Store Location: 123 Easy St.')
    # response.redirect('http://0.0.0.0:8005/twilio_bot/')



    # print(response)

    
    # response = MessagingResponse()
    # message_sent = Message()
    # message_sent.body('Hello World!')
    # response.append(message_sent)
    # response.redirect('http://0.0.0.0:8005/twilio_bot/')


    # print(response)
        # message_sent = "hello world"
        # headersss={ 
        #     'content-length': '5', 
        #     'content-type': 'application/json',
        #     'Accept':'application/json'
        # }

    # return redirect('http://0.0.0.0:8005/twilio_bot/',message_sent ='kkkkkk', headers={ 
    #         'content-length': '5', 
    #         'content-type': 'application/json',
    #         'Accept':'application/json'
    #     })
    # return redirect('http://0.0.0.0:8005/twilio_bot/',message_sent ='kkkkkk',headers={'Content-Type':'application/json','Accept':'application/json'})
    
# def someviews(request):
#     url = "http://0.0.0.0:8000/js/walker_run"        
#     return requests.get(url).json()











    # headers={'Content-Type':'application/json', 'Authorization':'Token 071ecdb2ab3f1a1a4c7a323caf17bba82516b7529d7302b06e3bd12de46a1180'}
    # headers={'Authorization':'Token 071ecdb2ab3f1a1a4c7a323caf17bba82516b7529d7302b06e3bd12de46a1180'}

    # return render(request, "http://0.0.0.0:8000/js/walker_run",
    # {
    #     "name": "talker",
    #     "ctx": {"question":"I would like a mohwk on monday at 6 pm"},
    #     "snt": "urn:uuid:51879472-1380-4848-8d2d-0b3bf3099588",
    #     "detailed": True
    # }, headers=headers)
    

# def jac_bot(request):
#     message = post wrokspace/js/


# sender message rediect to jac 
# function for message - pass message 
# function for twilio bot - receive from whatsapp - send to whatsapp
# function for jac bot - receive form jac - send to jac

    # if request.method == 'POST':
    #     send_question_jac

    # return redirect("http://0.0.0.0:8000/js/walker_run",
    # {
    #     "name": "talker",
    #     "ctx": {"question":"I would like a mohwk on monday at 6 pm"},
    #     "snt": "urn:uuid:51879472-1380-4848-8d2d-0b3bf3099588",
    #     "detailed": True
    # }, headers=headers)


# from twilio.rest import Client 
 
# account_sid = 'AC43ef78c7eeaed4a7946b247ece883c71' 
# auth_token = '[AuthToken]' 
# client = Client(account_sid, auth_token) 

# tes = "itwoek"
# message = client.messages.create( 
#                               from_='whatsapp:+14155238886',  
#                               body='Your {{tes}} code is {{2}}',      
#                               to='whatsapp:+5926431530' 
#                           ) 
 
# print(message)


# def send_question_jac(info):
    
#     response = MessagingResponse()
#     # message = Message()
#     # message.body('Hello World!')
#     # response.append(message)
#     response.redirect("http://0.0.0.0:8000/js/walker_run",
#     {
#         "name": "talker",
#         "ctx": {"question":"I would like a mohwk on monday at 6 pm"},
#         "snt": "urn:uuid:51879472-1380-4848-8d2d-0b3bf3099588",
#         "detailed": True
#     })

#     print(response)
# def redirect_view(request):
#     response = redirect('/redirect-success/')
#     return response

# https://youtu.be/G1AHluL0-fY
# python manage.py migrate
# python manage.py runserver 8090
# ngrok http 8000
