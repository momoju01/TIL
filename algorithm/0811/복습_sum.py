for T in range(10):
    tc = int(input())
    N = 100
    arr =[list(map(int, input().split())) for _ in range(N)]

    max1, max2, max3, max4 = 0, 0, 0, 0  # 최대값
    sum3, sum4 = 0, 0  # 합
    ans = 0

    # 행의 합 중 최대값
    for i in range(N):
        sum1 = 0
        for j in range(N):
            sum1 += arr[i][j]
            if sum1 > max1:
                max1 = sum1

    # 열의 합 중 최대값
    for j in range(N):
        sum2 = 0
        for i in range(N):
            sum2 += arr[i][j]
            if sum2 > max2:
                max2 = sum2

    # 우하향 대각선의 합 중 최대값
    for i in range(N):
        max3 += arr[i][j]

    # 대각선2의 합
    for i in range(N):
        max4 += arr[i][99-i]

    # 최대값 비교
    if max1 > ans:
        ans = max1
    if max2 > ans:
        ans = max2
    if max3 > ans:
        ans = max3
    if max4 > ans:
        ans = max4

    print(f'#{tc} {ans}')