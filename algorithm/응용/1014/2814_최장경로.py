def f(i, N, c):  # 가능한 모든 탐색
    global maxV
    if maxV < c + 1:
        maxV = c + 1
    visited[i] = 1
    for j in range(1, N+1):
        if adjM[i][j] == 1 and visited[j] == 0:
            f(j, N, c+1)
    visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adjM = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        n1, n2 = map(int, input().split())
        adjM[n1][n2] = 1
        adjM[n2][n1] = 1
    visited = [0] * (N+1)
    cnt = 0
    maxV = 0
    for i in range(1, N + 1):
        f(i, N, 0)
    print(f'#{tc} {maxV}')