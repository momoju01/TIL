import requests

# 기본 설정 ㅋㅋㅋ 실행 안 됨
TOKEN = '1877212350:AAFu4Hyr-Bwl6AwmUeSXRBlfy94kv02DhB0' # 문자열로 토큰 넣어 감싸주기
APP_URL = f'https://api.telegram.org/bot{TOKEN}'


# chat_id 가져오기
# https://api.telegram.org/bot1877212350:AAFu4Hyr-Bwl6AwmUeSXRBlfy94kv02DhB0/getUpdates
UPDATES_URL = f'{APP_URL}/getUpdates'
response = requests.get(UPDATES_URL).json() #jason은 가져오기 쉽게 정된됨.
# print(response) # 문법 print(response["ok"])

#chat id가 어디 있는지 print(response)에서 찾아서 get 함수로 가져오기
# {'ok': True, 'result': [{'update_id': 516070183, 'message': {'message_id': 1, 'from': {'id': 1727282774, 'is_bot': False, 'first_name': '윤하', 'last_name': '김'}, 'chat': {'id': 1727282774, 
chat_id = response.get('result')[0].get('message').get('chat').get('id')
print(chat_id)

text = '파이썬으로 보낸 메세지입니다.'
# https://api.telegram.org/bot1877212350:AAFu4Hyr-Bwl6AwmUeSXRBlfy94kv02DhB0/sendMessage?chat_id=1727282774&text=%EB%B3%B4%EB%82%B4%EC%A7%80%EB%82%98%EC%9A%94?
message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={text}' # 누구에게? chat_id={} 무엇을& text={}


requests.get(message_url) 




