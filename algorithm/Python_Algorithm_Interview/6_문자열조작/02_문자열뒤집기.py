"""
문자열을 뒤집는 함수 작성
입력 : 문자 배열 ??? 문자 배열 어떻게 입력시켜?
['h', 'e', 'l', 'l', 'o']
hello
리턴 없이 리스트 내부를 직접 조작
"""




# 0. 내 풀이
# new = []
# lst = list(input())
# for i in range(len(lst)-1, -1, -1):
#     new.append(lst[i])

# print(new)

# 1. swapping using two pointers
def reverseString(s):
    left, right = 0, len(s) -1
    while left < right: # 같으면 종료
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
        return s


# 2. pythonic !
def reversStringPythonic(s):
    s.reverse()
    return s

# 3. Slicing
def reverseStringSlicing(s):
    # s = s[::-1]   # -> 안 되는 플랫폼도 있음
    s[:] = s[::-1]  
    return s

text = ['h', 'e', 'l', 'l', 'o']

# print(reverseString(text))
# print(reversStringPythonic(text))
print(reverseStringSlicing(text))