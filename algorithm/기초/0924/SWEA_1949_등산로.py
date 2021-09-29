# def f(i, j, N, K, c, s):  # i,j칸이 등산로에 포함, 깎는 횟수 c, 이전까지의 길이 s
#     global maxV           # 최대 등산로 길이
#     if maxV < s + 1:
#         maxV = s + 1      # 최대 등산로 길이 갱신
#     v[i][j] = 1           # 현재 등산로에 포함된 칸
#
#     # 주변 칸 탐색
#     for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#         ni, nj = i +di, j +dj
#         if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
#             if arr[i][j] > arr[ni][nj]:  # 더 낮은 경우
#                 f(ni, nj, N, K, c, s+1)
#             elif c == 1 and arr[i][j] - K < arr[ni][nj]:  # 깎고 이동할 수 있는 경우
#                 # 깍기 전 높이 keep해둬야 나중에 원복 가능
#                 tmp = arr[ni][nj]
#                 arr[ni][nj] = arr[i][j] -1  # 내가 이동할 수 있는 최소한만큼(나보다 1작게) 깍기
#                 f(ni, nj, N, K, c-1, s +1)
#                 arr[ni][nj] = tmp
#     v[i][j] = 0   # i, j칸을 이전의 다른 경로에서 사용할 수 있도록
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # 내가 만들어 둔 등산로 깎지 않도록
#     v = [[0]*N for _ in range(N)]  # 현재 등산로에 포함된 칸 표시
#
#     # 가장 높은 봉우리 높이 찾기
#     h = 0      # 최대 높이
#     for i in range(N):
#         for j in range(N):
#             if h < arr[1][j]:
#                 h = arr[i][j]
#
#     # 가장 높은 곳에서 등산로 만들기
#     maxV = 0    # 최대 등산로 길이
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == h:
#                 f(i, j, N, K, 1, 0)     # i, j에서 등산로 만들어보기, 깎을 수 있는 횟수, 지금까지의 등산로 길이




dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, -1, 1]

# 1. 현재 위치를 들고 다니지 않을 때
# r, c : 좌표, road: 지금까지 조성된 등산로의 길이, skill: 공사 여부
def work(r, c, road, skill):
    global ans
    if road > ans:
        ans = road

    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            # a. 현위치보다 낮은 곳으로 이동할 때
            if mountain[r][c] > mountain[nr][nc]:
                work(nr, nc, road+1, skill)
            # b. 현위치보다 높거나 같은 곳으로 이동할 때
            elif skill and mountain[r][c] > mountain[nr][nc] - K:
                tmp = mountain[nr][nc]  # 기록
                mountain[nr][nc] = mountain[r][c] -1
                work(nr, nc, road+1, 0)  # 스킬 사용
                mountain[nr][nc] = tmp  # 원상 복구
    visited[r][c] = 0


# 2. 현재 위치 들고 다니면
def work2(r,c, h, road, skill):  # 현재 위치 h
    global ans
    if road> ans:
        ans = road
    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]: continue

        if h > mountain[nr][nc]:
            work2(nr, nc, mountain[nr][nc], road+1, skill)
        elif skill and h > mountain[nr][nc] - K:
            work2(nr, nc, mountain[r][c] -1, road +1, 0)

    visited[r][c] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N: 한 변의 길이, K: 최대 공사가 가능한 깊이

    #N*N 크기의 2차원 리스트(배열)이 주어진다.
    mountain = [list(map(int, input().split())) for _ in range(N)]

    max_h = 0      # 최대 높이
    # 가장 높은 봉우리 높이 찾기
    for i in range(N):
        for j in range(N):
            if max_h < mountain[1][j]:
                max_h = mountain[i][j]

    # mountain = []
    # max_h = 0
    # for i in range(N):
    #     # 한줄 입력 받고 내부에서 가장 큰 값 찾기
    #     tmp = list(map(int, input().split()))
    #
    #     for j in tmp:
    #         if max_h < j:
    #             max_h = j
    #
    #     mountain.append(tmp)

    visited = [[0]* N for _ in range(N)]
    ans = 0

    # 모든 가장 높은 봉우리에서 실행해봐야 함
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_h:  # 가장 높은 봉우리
               # work(i, j, 1, 1)  # 좌표, 길, 스킬
                work2(i,j, max_h, 1, 1)  # 좌표, 높이, 길, 스킬

    print("#{} {}".format(tc, ans))