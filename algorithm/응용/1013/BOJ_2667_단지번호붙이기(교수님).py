def dfs1(i, j ,N):
    global cnt
    visited[i][j] = 1
    cnt += 1
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <=ni < N and 0 <=nj < N and arr[ni][nj] and visited[ni][nj] == 0:
            dfs1(ni, nj, N)

def dfs2(i, j ,N):
    visited[i][j] = 1
    cnt = 1
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <=ni < N and 0 <=nj < N and arr[ni][nj] and visited[ni][nj] == 0:
            cnt += dfs2(ni, nj, N)
    return cnt



def bfs(i, j, N):
    cnt = 0
    q = [(i, j)]         # 큐 생성, 시작점 인큐
    visited[i][j] = 1    # 시작점 방문 표시
    while q:
        i, j = q.pop(0)
        # visited(i, j)
        cnt += 1         # 방문한 개수
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
    return cnt   # global 안 쓰고..

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

ans = 0
visited = [[0]*N for _ in range(N)]
block = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j] == 1:
            ans += 1  # 매번 시작할 때마다 탐색 수 셈(단지 수)

            # cnt = 0   # 한 단지 내 가구 수
            # dfs1(i, j, N)

            # cnt = bfs(i, j, N)
            cnt = dfs2(i, j, N)
            block.append(cnt)

print(ans)
block.sort()
for s in block:
    print(s)