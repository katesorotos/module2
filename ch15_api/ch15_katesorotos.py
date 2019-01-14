# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 13:50:43 2019

@author: Kate Sorotos
"""
import requests 

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/INSERT_DOMAIN_NAME_HERE/messages",
        auth=("api", "INSERT_API_KEY_HERE"),
        data={"from": "Excited User <kate.sorotos@bt.com>",
              "to":  ["seraphine.young@bt.com"],
              "subject": "Hello user",
              "text": "Lets see if this works! :)"})

send_simple_message()




