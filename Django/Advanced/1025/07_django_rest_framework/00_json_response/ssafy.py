import requests
from pprint import pprint

response = requests.get('http://127.0.0.1:8000/api/v1/json-3/')
# pprint(type(response.json()))

data = response.json()  #하나의 큰 리스트
pprint(data[0])