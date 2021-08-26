T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0

    for k in range(1, M+1):
        if M % k == 0 or k == M:
            # 전체 토글
            for i in range(N):
                for j in range(N):
                    if arr[i][j] == 1:
                        arr[i][j] = 0
                    else:
                        arr[i][j] = 1

        else:
            # i + j 랑 (i+j) % k == 0인 것만 토글하는데, i와 j가 1부터 시작하므로 1씩 더해줌
            for i in range(N):
                for j in range(N):
                    if (i +j + 2)% k == 0 or (i + j + 2) == k:
                        if arr[i][j] == 1:
                            arr[i][j] = 0
                        else:
                            arr[i][j] = 1

    for i in range(N):
        res += arr[i].count(1)
    print(f'#{tc} {res}')