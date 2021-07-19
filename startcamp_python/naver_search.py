import requests

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


message = f'{product_name}\n{product_price}\n{product_link}'
print(message)