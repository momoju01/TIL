for _ in range(10):
    tc = int(input())

    N = [list(map(int, input().split())) for _ in range(100)]
    max_a = 0  # 행의 최대값
    sum_a = 0  # 행의 합
    max_b = 0  # 열의 최대값
    sum_b = 0  # 열의 합
    max_c = 0  # 대각선1의 합
    max_d = 0  # 대각선2의 합
    ans = 0  # 최댓값

    # 각 행의 합
    for i in range(len(N)):
        sum_a = 0
        for j in range(len(N[i])):
            sum_a += N[i][j]
            if sum_a > max_a:
                max_a = sum_a

    # 각 열의 합
    for j in range(len(N[0])):
        sum_b = 0
        for i in range(len(N)):
            sum_b += N[i][j]
            if sum_b > max_b:
                max_b = sum_b

    # 대각선1의 합
    for i in range(len(N)):
        for j in range(len(N)):
            if i == j:
                max_c += N[i][j]

    # 대각선2의 합
    for i in range(len(N)):
        for j in range(len(N)):
            if i + j == len(N) - 1:
                max_d += N[i][j]

    # 최대값 비교
    if max_a > ans:
        ans = max_a
    if max_b > ans:
        ans = max_b
    if max_c > ans:
        ans = max_c
    if max_d > ans:
        ans = max_d

    print(f'#{tc} {ans}')