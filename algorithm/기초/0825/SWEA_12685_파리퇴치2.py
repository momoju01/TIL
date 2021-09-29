# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     maxV = 0
#
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             temp = 0
#             for k in range(M):
#                 for l in range(M):
#                     if k == l or k + l == M-1:
#                         temp += arr[i+k][j+l]
#             if temp > maxV:
#                 maxV = temp
#
#
#     print(f'#{tc} {maxV}')



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):              # 좌상향: k, l(=M-1-k)
                temp += arr[i+k][j+k]
                temp += arr[i+k][j+M-1-k]
            if M % 2:                        # M이 홀수일 때 중복으로 더해짐
                temp -= arr[i+M//2][j+M//2]  # 중복 제거
            if temp > maxV:
                maxV = temp

    print(f'#{tc} {maxV}')