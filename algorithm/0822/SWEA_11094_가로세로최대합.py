T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    for i in range(N):
        for j in range(N):
            temp = 0
            for k in range(N):
                temp += arr[i][k]
                temp += arr[k][j]
            temp -= arr[i][j]     # 중복으로 더해진 부분 빼주기
            if temp > maxV:
                maxV = temp

    print(f'#{tc} {maxV}')