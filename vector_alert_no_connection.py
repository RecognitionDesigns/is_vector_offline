#!/usr/bin/env python3

import http.client, urllib
from keys import (token, user)
import random
import os

def send_alert():
    n1 = ['Hello.','Hi.','Howdy.','Good day.','Greetings.','Alert!']
    n2 = ['is not responding -','is offline -','is unreachable -','has lost connection -','is DEAD! -', 'has dropped out -','is sleeping with the fishes -','is pushing up roses -','has gone AWOL -','is not alive -','non-operational -']
    n3 = ['Please help!','Send Watts','Plug him in.','Save him!']

    alert_message1 = (random.choice(n1),'Vector',random.choice(n2),random.choice(n3))
    alert_message = (str(alert_message1).replace(",", "").replace("'", "").replace("(", "").replace(")", ""))

    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.parse.urlencode({
        "token": token,
        "user": user,
        "message": (alert_message)
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
    
try:
    if os.system("cd ~/alert_run_once/") != 0:
        raise Exception('folder does not exist')

except:
    print("Running for the first time")
    os.system("cd ~/ && sudo mkdir alert_run_once")
    send_alert()


else:
    print("Not the first time...")
