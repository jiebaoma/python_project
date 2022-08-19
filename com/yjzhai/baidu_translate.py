#!/usr/bin/python
import requests
from urllib import parse

data={'city':'北京'}
city=parse.urlencode(data).encode('utf-8')
url='http://www.sojson.com/open/api/weather/json.html'

r=requests.get(url,params=city)

response_data=r.json()

print(response_data['data'])
print(response_data['message'])
print(response_data['status'])
print(response_data['city'])

print(response_data['data']['forecase'][0]['data'])
print(response_data['data']['forecase'][0]['type'])
print(response_data['data']['forecase'][0]['high'])
print(response_data['data']['forecase'][0]['low'])