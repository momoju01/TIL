import requests


#네이버에서 필요한 것 찾아서 보낼 메시지 만들기
# naver 요청 보낼 때 필요한 것들
naver_client_id = '93pVFcaR1qV7P5qdcK43'
naver_client_secret = 'pljZFY2fTt'
URL = 'https://openapi.naver.com/v1/search/shop.json?query={}'


#x토큰 같은 개념. 출입증 만든 것 
headers = {
'X-Naver-Client-Id':  naver_client_id,
'X-Naver-Client-Secret': naver_client_secret
}

query ='ps5'


product = requests.get(URL+query, headers=headers).json()['items'][0]  #url 뒤에 ps5가 따라가서 붙음. 출입증도 같이 보내기~
# print(product)
product_name = product['title']
# print(product_name)
product_price = product['lprice']
# print(product_price)
product_link = product['link']
# print(product_link) 

message = f'이름 : {product_name}\n 가격 : {product_price}\n 링크 :{product_link}' # 요 메시지를 텔레그램으로 보내고 싶음! 
# print(message)



# 텔레그램에서 메세지 보내기
# 텔레그램 기본 사항

TOKEN = '1877212350:AAFu4Hyr-Bwl6AwmUeSXRBlfy94kv02DhB0' # 문자열로 토큰 넣어 감싸주기
APP_URL = f'https://api.telegram.org/bot{TOKEN}'

# chat_id 가져오기
# https://api.telegram.org/bot1877212350:AAFu4Hyr-Bwl6AwmUeSXRBlfy94kv02DhB0/getUpdates
UPDATES_URL = f'{APP_URL}/getUpdates'
response = requests.get(UPDATES_URL).json() #jason은 가져오기 쉽게 정된됨.
# print(response["ok"]) # 문법 print(response["ok"])

chat_id = response.get('result')[0].get('message').get('chat').get('id')
# print(chat_id)

# text = '파이썬으로 보낸 메세지입니다.' << 이거 대신 m

# https://api.telegram.org/bot1877212350:AAFu4Hyr-Bwl6AwmUeSXRBlfy94kv02DhB0/sendMessage?chat_id=1727282774&text=%EB%B3%B4%EB%82%B4%EC%A7%80%EB%82%98%EC%9A%94?
message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={message}'  # naver편에서 만든 message 를 보내기~!

requests.get(message_url)