"""
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
대소문자를 구분하지 않으며, 구두점 또한 무시한다.
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
"""
import re
import collections
# data cleansing (Preprocessing)
par = "Bob hit a ball, the hit BALL flew far after it was hit."
ban = ["hit"]

def mostCommonWord(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)  # \w: 문자, ^:not -> 단어 문자가 아닌 모든 문자를 공백으로 치환(Substitute)
             .lower().split()
                if word not in banned]  # 조건절 : banned에 없는 단어만
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]  # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴! [('ball', 2)]의 형태로 저장되어있음

print(mostCommonWord(par, ban))