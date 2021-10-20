"""
팰린드롬 여부 판별
대소문자 구분x, 영문과 숫자 대상
A man, a plan, a canal: Panama

"""
from collections import deque
import re

# 풀이 1: 리스트로 변환
def isPalindrome(s):
    strs = []
    for char in s:
        if char.isalnum():  # 영문자와 숫자 판별하는 함수로, 해당하는 문자만 추가
            strs.append(char.lower())  # 모두 소문자로 변환

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():  # 맨앞과 맨 뒤 pop 해서 같지 않다면
            return False
        return True


# 풀이2: 데크 자료형을 이용한 최적화

def isPalindrome_deque(s):
    strs = deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
        return True



def isPalindrome_slicing(s):
    s = s.lower
    # 정규식으로 불필요한 문자 필터링하기  
    s = re.sub('[^a-z 0-9]', '', s)  # < 이거 뭔가 이상함. 일단 중요한 건 슬라이싱이니까 넘어가기

    return s == s[::-1] # 슬라이싱

text = input()

# print(isPalindrome(text))
# print(isPalindrome_deque(text))
print(isPalindrome_slicing(text))