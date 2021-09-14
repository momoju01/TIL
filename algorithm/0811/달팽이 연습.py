T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]  # 달팽이 배열

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    cnt = 1  # 1부터 기록 예정
    i, j = 0, -1
    k = 0   #방향 : di 와 dj 요소 가리기는 용도. 0~4: 시계방향

    while cnt <= N * N:
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            arr[ni][nj] = cnt
            cnt  += 1
            i, j = ni, nj
        else:
            k = (k + 1) % 4  # 방향 변경

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i], end=" ")
        print()

