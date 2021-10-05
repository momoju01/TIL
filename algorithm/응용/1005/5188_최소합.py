"""
그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고,
다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13
"""


def f(x, y, cnt):
    global minV
    if x == N-1 and y == N-1:  # 도착
        if cnt < minV:
            minV = cnt
        return
    else:
        if cnt >= minV:
            return
        else:
            # 우 / 하 only라서 visited 확인 생략
            dx, dy = [0, 1], [1, 0]
            for k in range(2):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    f(nx, ny, cnt + arr[nx][ny])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 10 * N * N

    f(0,0, arr[0][0])

    print(f'#{tc} {minV}')