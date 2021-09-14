T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    arr_90 = [[0]*N for _ in range(N)]
    arr_180 = [[0]*N for _ in range(N)]
    arr_270 = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr_90[i][j] = arr[N-1-j][i]
            arr_180[i][j] = arr[N-1-i][N-1-j]
            arr_270[i][j] = arr[j][N-1-i]


    # 출력
    print(f'#{tc}')
    for i in range(N):
        print(''.join(arr_90[i]), ''.join(arr_180[i]), ''.join(arr_270[i]))


