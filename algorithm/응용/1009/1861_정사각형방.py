import sys
sys.stdin = open('input_2819.txt', 'r')

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def f(r, c, num):
    global visited
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if num + 1 == arr[nr][nc]:
                visited[num] = 1
                f(nr, nc, num+1)

def check():
    for i in range(1000, -1, -1):
        if visited[i]:
            cnt += 1
            st = i
        if cnt > maxV:
            maxV = cnt
            st = i


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * 1000

    for i in range(N):
        for j in range(N):
            f(i, j, arr[i][j])

    f()

