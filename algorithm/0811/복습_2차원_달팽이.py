T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]  # 배열 0으로 초기화

    r = 0  # 헹 시작 위치
    c = 0  # 열 시작 위치
    value = 1  # 배열에 넣을 값. 1 ~ N*N까지
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    f = 0  #flag

    while value <= 25:  # 1~N*N까지 실행
        arr[r][c] = value  # 현위치 (0,0)에  1 넣어줌

        nr = r + dr[f]  # 새로운 위치로 이동
        nc = c + dc[f]

        # 조건 만족하지 않는 경우
        if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc]:
            f = (f + 1)% 4  # 방향 변경

        # 죄표를 갱신한다.
        r += dr[f]
        c += dc[f]

        # value를 증가시킨다.
        value += 1

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i], end=' ')
        print()

