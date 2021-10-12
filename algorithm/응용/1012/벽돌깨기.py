def bomb(y, x):
    global H, W
    val = dest[y][x]
    dest[y][x] = 0

    for len in range(1, val):
        for dir in range(4):
            ny = y + len * dy[dir]
            nx = x + len * dx[dir]

            if 0 <= ny <= H - 1 and 0 <= nx <= W - 1 and new[ny][nx] != 0:
                bomb(ny, nx)

def f(org, N, W, H):  # org: 발사 전 벽돌 상태, N남은 발사 횟수
    global minV
    if N == 0:  # 남은 발사횟수가 없으면 남은 벽돌 세기
        cnt = 0
        for i in range(H):
            for j in range(W):
                if org[i][j]:  # 벽돌 남아있다면
                    cnt += 1
        if minV > cnt:
            minV = cnt
    else:  # 구슬을 발사할 수 있으면
        for k in range(W):  # k 구슬을 발사할 위치
            dest = [[0]*W for _ in range(H)]
            for i in range(H):  # 구슬을 복사할 복사본 만들기
                for j in range(W):
                    dest[i][j] = org[i][j]
                    # 발사....
                    bomb(i, j)
            # N-1
            f(dest, N-1, W, H)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    minV = W*H  # 최소로 남은 벽돌
    f(A, N, W, H)  # 남은 발사 횟수