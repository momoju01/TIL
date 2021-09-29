# 크기 n 의  파스칼의 삼각형

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [([1]+ [0] * (N-1)) for _ in range(N)]  # N*N 배열 생성

    for i in range(1, N):
        for j in range(1, N):
            arr[i][j] =  arr[i-1][j-1] + arr[i-1][j]


    # 0 제외하고 출력
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                print()
                break
            else:
                print(arr[i][j], end=' ')
    print()


