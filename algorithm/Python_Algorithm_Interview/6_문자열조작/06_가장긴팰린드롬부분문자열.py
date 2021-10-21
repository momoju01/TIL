# Longest Palindrome Substring

"""
input: babad
output: bab
> aba도 정답
"""

# 1. 중앙을 중심으로 확장하는 풀이
def longestPalindrome(s):

    def expand(left, right): # 확장
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left +1 : right]

    # 해당사항이 없을 때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s)-1):
        result = max(result,
                     expand(i, i+1),
                     expand(i, i+2),
                     key=len)
        return result


print(longestPalindrome("babad"))