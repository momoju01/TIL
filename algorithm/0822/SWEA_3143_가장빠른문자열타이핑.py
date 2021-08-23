T = int(input())

for tc in range(1, T+1):
    str1, str2 = input().split()
    len1, len2 = len(str1), len(str2)
    typing = len1

    for i in range(len1-len2+1):
        cnt = 0
        for j in range(len2):
            if str2[j] == str1[i+j]:
                cnt += 1
        if cnt == len2:
            typing -= len2 -1
    print(f'#{tc} {typing}')

