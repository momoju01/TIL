import sys
sys.stdin = open('input_2819.txt', 'r')


# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c, num):  # 좌표, 7자리 숫자
    # 완성시
    if len(num) == 7:
        ans.add(num)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            dfs(nr, nc, num + arr[nr][nc])


T = int(input())
for tc in range(1, T+1):
    N = 4
    arr = [input().split() for _ in range(N)]  # string으로 받기
    ans = set()

    for i in range(N):
        for j in range(N):
            dfs(i, j, arr[i][j])

    print(f'#{tc} {len(ans)}')