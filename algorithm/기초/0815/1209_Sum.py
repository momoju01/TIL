for T in range(1, 11):
    tc = '#'+input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0

    # 행의 합
    for i in range(100):
        temp_sum = 0
        for j in range(100):
            temp_sum += arr[i][j]

        if temp_sum > max_sum:
            max_sum = temp_sum

    # 열의 합
    for j in range(100):
        temp_sum =0
        for i in range(100):
            temp_sum += arr[i][j]

        if temp_sum > max_sum:
            max_sum = temp_sum

    # 우하향 대각선 합 i = j
    for _ in range(0):
        temp_sum = 0
        for j in range(100):
            temp_sum += arr[i][i]

        if temp_sum > max_sum:
            max_sum = temp_sum

    # 우상향 대각선의 합 j = N - i + 1
    for _ in range(0):
        temp_sum = 0
        for i in range(100):
            temp_sum += arr[i][99-i]
        if temp_sum > max_sum:
            max_sum = temp_sum

    print(f'{tc} {max_sum}' )