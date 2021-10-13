# 현재 방향 아니면 다음 방향만 보면 됨
# 1. 완전탐색
# 2. 방향 기억하기
# 좌하, 우하, 우상, 좌상
dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]


def dfs(x, y, c, f):  #
    global maxV, si, sj
    # 종료조건
    if k == 3 and x == si and y == sj:  # 출발 지점에 도착
        if maxV < c :  # 대소 비교
            maxV = c
            return
    elif x < 0 or x >=N or y < 0 or y >= N:  # 범위 벗어난 경우 리턴
        return
    elif arr[x][y] in tmp:  # 디저트 숫자가 중복인 경우
        return
    #
    else:
        tmp.append(arr[x][y])
        if k == 0 or k == 1:  # 왼쪽으로 쭉 가거나 오른쪽으로 꺾었을 때
            dfs(x + dx[f], y + dy[f], c+1, k)  #
        nx, ny = x + dx[f], y + dy[f]
        dfs(nx, ny, c, tmp)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tmp = []
    for i in range(N):
        for j in range(1, N-1):  # 맨 바깥쪽은 돌 필요 x
            si, sj = i, j  # 시작 인덱스
            tmp.append(arr[i][j])
            dfs()
