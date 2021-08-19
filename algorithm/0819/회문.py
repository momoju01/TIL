# T = int(input())
#
# for T in range(1, T+1):
#     tc = T
#     N, M = map(int, input().split())  # N: N*N 배열 M: 회문 길이
#     arr = [list(input()) for _ in range(N)]
#     pal = ''
#
#     # 행
# ans = -1
# for j in range(N - M + 1):
#     cnt = 0
#     for k in range(M // 2):
#         if arr[i+j] == arr[i+M-1-j]:
#             break
#     else:
#         ans = i
#         break
# if ans != -1 :
#
#
# print(f'#{tc} {ans}')

ans = -1
for i in range(N-M + 1):
    flag = 1
    for j in range(M//2):
        if str1[i + j] != str[i + M -1-j]:
            flag = 0  # i에서 시작하는 구간은 회문이 아님
            break
    if flag == 1:  # i에서 시작하는 회문
        ans = i
        break


if ans != -1 :
    for k in range(M):
        print(str1[ans+k], end='')
    print()
else:
    ans = -1