T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    res = 0

    for i in range(N):
        for j in range(N):
            for f in range(4):  # di dj 리스트에서 flag
                ni, nj = i + di[f], j + dj[f]
                # 범위 확인하고 차의 절대값
                if 0 <= ni < N and 0 <= nj < N:
                    res += abs(arr[i][j]- arr[ni][nj])

    print(f'#{tc} {res}')



