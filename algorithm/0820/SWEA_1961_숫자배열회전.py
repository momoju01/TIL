T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]



    def rotate_90(N, arr):
        rotated = [[0]*N for _ in range(N)]
        for i in range(N):          # i : 0~2
            for j in range(N-1, -1, -1):  # j : 2~0
                rotated[i][j]