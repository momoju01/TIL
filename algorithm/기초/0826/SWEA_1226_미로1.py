def func(a, b):
    visited[a][b] = 1
    for da, db in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 각 방향별로 돌 예정
        na, nb = a + da, b + db
        if arr[na][nb] != '1' and not visited[na][nb]:
            func(na, nb)


for tc in range(10):
    idx = int(input())
    arr = [input() for i in range(16)]
    visited = [[0 for i in range(16)] for j in range(16)]
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    sj, si, ei, ej = 0, 0, 0, 0

    # 시작& 끝 인덱스 찾기
    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                sj, si = i, j
            if arr[i][j] == '3':
                ei, ej = i, j

    func(si, sj)

    print(f'#{tc + 1} {visited[ei][ej]}') # 마지막 위치 방문 여부

