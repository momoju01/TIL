


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0 # 모든 원소에 대해, 주변 원소와의 차이의 절대값의 합
    for i in range(N):
        for j in range(N):  #N*N배열이라
            for di, dj, in [(0,1), (1,0), (0, -1), (-1,0)]:
                ni, nj = i+ di, j + dj  # i, j 의 주변 값들 나타내는 인덱스
                if 0 <= ni < N and 0 <= nj < N: # 배열을 벗어나지 않으면
                     ans += abs(arr[i][j]-arr[ni][nj])
    print(f'#{tc} {ans}')


