def solve(r, c, dir, l):  # dir: 방향, l: 움직인 거리(반복문이면 필요없는 인자들임)
    ## 재귀

    # 더 이상 탐색을 수행하지 않아도 되는 경우
    # 1. 도착 지점에 도착했을 때
    # 2. 디저트 번호가 중복될 때
    global maxV
    # 종료조건
    if dir == 3 and r == si and c == sj:  # 출발 지점에 도착
        if maxV < l:  # 대소 비교
            maxV = l
            return
    elif r < 0 or r >= N or c < 0 or c >= N:  # 범위 벗어난 경우 리턴
        return
    elif arr[r][c] in tmp:  # 디저트 숫자가 중복인 경우
        return

    else:
        # 현재 위치 도착: dfs -  완전탐색 (현재 상황에서 내가 할 수 있는 모든 경우의 수 실행)
        # 직진하다가 방향 바꾸거나 계속 직진하는 것
        # 방향에 따른 할 수 있는 경우의 수 구분하기
        tmp.append(arr[r][c])
        if dir == 0:  # 좌측 하단으로 이동
            # 좌하로 계속이동
            solve(r+dr[0], c+dc[0], 0, l+1)
            # 우하로 이동
            solve(r+dr[1], c+dc[1], 1, l+1)
        elif dir == 1:  # 우하로 이동
            # 우하로 계속 이동
            solve(r + dr[1], c + dc[1], 1, l + 1)
            # 우상으로 이동
            solve(r + dr[2], c + dc[2], 2, l + 1)
        elif dir == 2:  # 우상으로 이동
            # 우상으로 계속 이동 (일단 직진)
            if si - sj != r - c:
                solve(r + dr[2], c + dc[2], 2, l + 1)
            # 좌상으로 이동 : 시작점 만날 것 같으면 좌상이동
            elif si - sj == r - c:
                solve(r + dr[3], c + dc[3], 3, l + 1)
        else:  # 좌상 이동
            # 직진 only
            if 0 <= r - 1 < N and 0 <= c - 1 < N:
                solve(r + dr[3], c + dc[3], 3, l + 1)
        tmp.remove(arr[r][c])

# 모든 칸에 대해서 순회
# 방향: 좌하, 우하, 우상, 좌상
dr = [1, 1, -1, -1]
dc = [-1, 1, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = -1
    tmp = []



    for i in range(N):
        for j in range(N):
            si, sj = i, j
            solve(i, j, 0, 0)

    print(f'#{tc} {maxV}')