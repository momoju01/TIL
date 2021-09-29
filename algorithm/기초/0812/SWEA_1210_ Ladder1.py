for tc in range(10):
    TC = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착점 좌표 찾기
    row = 99
    col = 0
    for i in range(100):
        if arr[99][i] == 2:
            col = i


    # 열 위치 0 될 때까지 반복
    while row >= 0:
        # 좌측 칸 좌표가 범위 안인지, 좌측에 1 있는지 검사:
        if (col - 1) >= 0 and arr[row][col - 1] == 1:
            col -= 1
            # 좌측 칸 좌표가 범위 안인지, 위가 0으로 막혀있는지 검사:
            while (col - 1) >= 0 and arr[row-1][col] == 0:
                col -= 1
            else:  # 막혀있거나 위가 1으로 길이 있으면 위로
                row -= 1

        # 우측 검사
        elif (col + 1) <= 99 and arr[row][col + 1] == 1:
            col += 1
            while (col + 1) <= 99 and arr[row-1][col] == 0:
                col += 1
            else:
                row -= 1
        # 아무 것도 해당 안 될 경우 위로
        else:
            row -= 1

    print(f'#{TC} {col}')

