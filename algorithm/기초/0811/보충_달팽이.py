T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    curR = 0
    curC = 0
    value = 1
    arr = [[0]*N for _ in range(N)]


    # 우 하 좌 상
    drow = [0, 1, 0, -1]
    dcol = [1, 0, -1, 0]
    mode = 0

    while value <= N * N:  # N^2칸 돌 것임
        # 1. 현재의 좌표에 value를 입력한다
        arr[curR][curC] = value

        # 2. 다음 데이터 입력을 위하여 좌표를 갱신한다.
        # 2-1. 갱신을 위한 새로운 좌표를 만든다
        newR, newC = curR + drow[mode], curC + dcol[mode]
        # 2-2. 새로운 좌표가 유효한지 확인한다.
        #     if 0 <= curR <= N and 0 <= curC <= N and value <= N

        # 2-3. 유효하지 않은 경우  mode 변경한다.
        if newR < 0 or newR >= N or newC <0 or newC >= N or arr[newR][newC]:
            mode = (mode+1) % 4
        # 2-4. 죄표를 갱신한다.
        curR += drow[mode]
        curC += dcol[mode]
        # 3. value를 증가시킨다.
        value += 1

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i], end=" ")
        print()
