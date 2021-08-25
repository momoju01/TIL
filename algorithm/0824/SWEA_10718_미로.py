# 출구를 찾으면 중단하는 함수
def f2(i, j, N):
    if maze[i][j] == 3:  # 3이면 도착
        return 1
    else:
        maze[i][j] = 1  # i, j 방문 표시
        for di, dj in [(0,1), (1, 0), (0, -1), (-1, 0)]:  # 우하좌상으로 돌면서 진행가능한 칸 확인
            ni, nj = i + di, j+ dj
            # 탐색 방향이 통로이면
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 0:
                if f2(ni, nj, N): return 1
            # 마지막 칸에 도착하면
            elif 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 3:
                return 1
        return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # N*N 미로
    maze = [list(map(int, input())) for _ in range(N)]
    si, sj = 0, 0
    # 시작 위치 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j

    print(f'#{tc} {f2(si, sj, N)}')