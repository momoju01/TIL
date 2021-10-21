arr = ["eat", "tea", "tan", "ate", "nat", "bat"]


# 1. 정렬하여 딕셔너리에 추가
import collections

def groupAnagrams(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

# print(groupAnagrams(arr))
#
# # 1. 풀어서 :
# anagrams = collections.defaultdict(list)
# for word in arr:
#     sorted(word)                                  # ['a', 'e', 't'] 한 단어 안에서 정렬
#     ''.join(sorted(word))                         # aet : ''.join() 한 값을 key값으로하고
#     anagrams[''.join(sorted(word))].append(word)  # value:['eat', 'tea', 'ate'] 원래 단어를 value로 append
#     # print(anagrams)                             # {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
# print(list(anagrams.values()))  # value만 list로 출력하기


## 여러 가지 정렬 방법

# sorted(list)
a = [2, 5, 1, 9, 7]
print(sorted(a))  # [1, 2, 5, 7, 9]

# sorted(str)
b = "zbdaf"
print(sorted(b))  # ['a', 'b', 'd', 'f', 'z']
print(b)          # zbdaf
print("".join(sorted(b)))  # abdfz

# list.sort() : 리스트 자체 정렬
a.sort()
print(a)  # [1, 2, 5, 7, 9]

# 옵션 지정해 정렬 key = len
c = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(c, key=len))  # ['d', 'bb', 'ccc', 'aaaa']

# 함수를 이용해 키 정의
d = ['cde', 'cfc', 'abc']
def fn(s):
    return s[0], s[-1]     # 첫 문자열, 마지막 문자열 순 정렬

print(sorted(d, key=fn))   # ['abc', 'cfc', 'cde']
print(sorted(d))           # ['abc', 'cde', 'cfc']