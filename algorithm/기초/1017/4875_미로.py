"""
5
13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.
"""

def dfs(i, j, N):
    # 종료조건 : 3
    if arr[i][j] == 3:
        return 1
    else:
        arr[i][j] = 1  # i, j 방문 표시 (바로 1로 변경해도됨)
        for di, dj in [(0,1), (1, 0), (0, -1), (-1, 0)]:  # 우하좌상
            ni, nj = i + di, j + dj
            # 탐색 방향이 통로(0)인 경우
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                if dfs(ni, nj, N): return 1  # ni, nj에서 탐색한 곳이 종료조건에 해당해서 1 return한다면 1 리턴하고 종료
                # 마지막 칸에 도착하면
            elif 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 3:
                return 1
        return 0

# visited 사용
def dfs2(i, j):
    if arr[i][j] == 3:
        return 1
    else:
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 우하좌상
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:  # 범위 안이고 방문 안 했으면
                if not arr[ni][nj]:                          # 통로이면
                    visited[ni][nj] = 1                      # 방문표시하고
                    if dfs2(ni,nj):                          # ni, nj 로 다시 dfs2 돌려서 return값 확인
                        return 1
                elif arr[ni][nj] == 3:
                    return 1
        return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    si, sj = 0, 0

    # 시작 위치 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j

    print(f'#{tc} {dfs(si, sj)}')
    # print(f'#{tc} {dfs2(si, sj)}')
