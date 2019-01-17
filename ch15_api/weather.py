# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:35:02 2019

@author: Kate Sorotos
"""

import requests 

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units":"metric", "appid":"INSERT_API_KEY_HERE"}
response = requests.get(endpoint, params = payload)
data = response.json()

print('This is what data looks like: \n')
print(data)

print()
print(response.url)
print(response.status_code)
print(response.headers["content-type"]) 