def solution(i, t, n):
    global minV
    if n == N - 1:
        t += arr[i][0]
        if minV > t:
            minV = t
    elif t > minV:
        return
    else:
        for j in range(1, N):
            if visited[j] == 0:
                visited[j] = 1
                solution(j, t + arr[i][j], n + 1)
                visited[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    minV = 0
    for _ in range(N):
        tmp = list(map(int, input().split()))
        minV += sum(tmp)
        arr.append(tmp)
    visited = [0] * N
    visited[0] = 1
    solution(0, 0, 0)
    print(f'#{tc} {minV}')