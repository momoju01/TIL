def bfs(i, j):
    q = [(i, j)]            # 큐 생성, 시작점 인큐
    visited[i][j] = 0       # 시작점 방문표시
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 우하좌상
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                # 새 좌표와 현 좌표 사이에 높이 차이가 나면
                if arr[ni][nj] > arr[i][j]:
                    tmp = visited[i][j] + 1 + (arr[ni][nj] - arr[i][j])  # 새 좌표와 현 좌표 간 높이 차를 가중치로 더해줌
                else:
                    tmp = visited[i][j] + 1
                if visited[ni][nj] > tmp:
                    visited[ni][nj] = tmp
                    q.append((ni, nj))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr =[list(map(int, input().split())) for _ in range(N)]
    visited = [[987654321] * N for _ in range(N)]
    bfs(0, 0)
    print(f'#{tc} {visited[N-1][N-1]}')
