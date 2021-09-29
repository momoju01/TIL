# 경로까지 가는 거리 찾는 함수

def f(i, j, N):
    q = []
    visited = [[0] * N for _ in range(N)]
    q.append((i, j))  # 시작점 인큐
    while q:
        a, b = q.pop(0)
        # 종료 조건
        if maze[a][b] == 3:
            return visited[a][b]-1

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = a + di, b + dj
            # 범위 이내이고, 벽이 아니고, 방문 안 했던 곳
            if 0 <= ni < N and 0<= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                # 새로 방문할 ni,nj좌표에 대한 visited표시는
                # 지금 큐에서 꺼내봤던 현재좌표 (a, b)에서 1거리만큼 떨어진 곳임을 표시
                visited[ni][nj] = visited[a][b] + 1
    # while 문 다 돌았는데 break 안 되고 끝나면 도착지에 도달 못한 것
    return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작 & 끝 위치 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
    print(f'#{tc} {f(si, sj, N)}')

