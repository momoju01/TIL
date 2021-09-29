"""
# 출발 0, 0 도착 7, 7
# 경로 있음, 경로 없음, 경로가 여러 개
3
8
0 0 1 1 1 1 1 1
1 0 0 0 0 0 0 1
1 1 1 0 1 1 1 1
1 1 1 0 1 1 1 1
1 0 0 0 0 0 0 1
1 0 1 1 1 1 1 1
1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 0
8
0 0 1 1 1 1 1 1
1 0 0 0 0 0 0 1
1 1 1 0 1 1 1 1
1 1 1 0 1 1 1 1
1 0 0 0 0 0 0 1
1 0 1 1 1 1 1 1
1 0 1 0 0 0 0 0
1 1 1 1 1 1 1 0
8
0 0 1 1 1 1 1 1
1 0 0 0 0 0 0 1
1 0 1 0 1 1 1 1
1 0 1 0 1 1 1 1
1 0 0 0 0 0 0 0
1 0 1 1 1 1 1 0
1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 0
"""


# 모든 칸을 방문하는 탐색
def f1(i, j, N):
    maze[i][j] = 2  # i, j 방문 표시
    for di, dj in [(0,1), (1,0), (0, -1), (-1, 0)]:  # 각 방향별로 돌 예정
        ni, nj = i + di, j + dj
        # 탐색 방향이 통로이면
        if 0<= ni<N and 0<=nj<N and maze[ni][nj]==0:  #and visited[ni][nj]
            f1(ni, nj, N)


N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
f1(0, 0, N)  # 탐색 시작(0, 0), N : 미로의 크기
print(maze[N-1][N-1])




# 출구를 찾으면 중단
def f2(i, j, N):  # 출구를 찾으면 중단
    if i==N-1 and j==N-1:   # 출구에 도착한 경우
        return 1
    else:
        maze[i][j] = 1  # i, j 방문표시. (진입한 칸을 벽으로 변경)
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4방향 탐색
            ni, nj = i + di, j + dj
            # 탐색 방향이 통로이면
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 0:  # and visited[ni][nj]==0
                if f2(ni, nj, N): # 출구를 찾고 리턴하면
                    return 1        # 입구까지 리턴(남겨둔 갈림길을 탐색하지 않음)
        return 0                # 탐색 방향에서 출국를 찾지 못한 경우

N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
print(f2(0, 0, N))




# 입구 > 출구 경로의 개수
# 모든 경로 탐색
def f3(i, j, N): # 입구-> 출구 경로의 개수
    global  cnt
    if i == N-1 and j == N-1:
        cnt += 1                # 경로에 도착한 횟수
        return
    else:
        maze[i][j] = 2  # 없으면 무한 루프의 위험
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4방향 탐색
            ni, nj = i + di, j + dj
            # 탐색 방향이 통로이면
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 0:  # and visited[ni][nj]==0
                f3(ni, nj, N)
        maze[i][j] = 0  # 다른 경로에서의 i, j 진입은 허용

N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
f3(0, 0, N)
print(cnt)


# 최단거리 (c: 지나온 칸의 개수)
# 모든 경로 탐색
def f4(i, j, N, c):  # 입구-> 출구 경로의 개수
    global minV
    if i == N - 1 and j == N - 1:
        if minV > c+1:    # 기존 경로보다 도착지 포함 경로의 길이가 더 짧으면
            minV = c+1    # c+1 출발, 도착을 포함한 경로의 길이
        return
    else:
        maze[i][j] = 2  # 없으면 무한 루프의 위험
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4방향 탐색
            ni, nj = i + di, j + dj
            # 탐색 방향이 통로이면
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 0:  # and visited[ni][nj]==0
                f4(ni, nj, N, c+1)  #
        maze[i][j] = 0  # 다른 경로에서의 i, j 진입은 허용

N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
minV = N * N
f4(0, 0, N, 0)
print(cnt)