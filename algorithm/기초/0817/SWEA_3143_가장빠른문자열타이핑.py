# result = len(str1) - str1.count(str2) * (len(str2) -1)

T = int(input())
for tc in range(1, T+1):
    str1, str2 = input().split()
    len1 = len(str1)
    len2 = len(str2)
    cnt = len(str1)  # str1에서 key 제외 예정
    i = 0

    while i <= len1 - len2 :  # 범위 내에서
        word = str1[i : i + len2]  # str2의 길이만큼 슬라이싱
        if word == str2:
            cnt -= len2 - 1  #일치하는 만큼 len1의 길이에서 1만 남기고 빼줌
            i = i + len2
        else:
            i += 1

    print(f'#{tc} {cnt}')





