T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())  # M은 파리채 중심~끝 크기
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    for i in range(N):      # 일부 벗어나도 되므로 전체 행렬 고려
        for j in range(N):
            cross, diag = arr[i][j],  arr[i][j]
            for k in range(1, M):  # 해당 칸 포함해서 사방 M 만큼 퇴치
                di, dj = [0, k, 0, -k], [k, 0, -k, 0]       # 우하좌상
                dx, dy = [-k, k, k, -k], [k, k, -k, -k]     # 우상 우하 좌하 좌상
                for f in range(4):
                    ni, nj = i + di[f], j + dj[f]
                    nx, ny = i + dx[f], j + dy[f]
                    if 0 <= ni < N and 0 <= nj < N:
                        cross += arr[ni][nj]
                    if 0 <= nx < N and 0 <= ny < N:
                        diag += arr[nx][ny]
            if cross > maxV:
                maxV = cross
            if diag > maxV:
                maxV = diag

    print('#{0} {1}'.format(tc, maxV))