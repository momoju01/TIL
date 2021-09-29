# N * N 배열
# M * M 파리채
# 한번 내려쳐 최대한 많은 파리 죽이기
# 답 : 죽은 파리 개수

# 5 < N < 15
# 2 < M < N
# max(파리 개수) = 30

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxKill = 0

    # 전체 면적
    for i in range(N - M + 1):  # i 왼쪽 위 기준
        for j in range(N - M + 1):
            kill = 0

            # 파리채 면적
            for k in range(M):
                for l in range(M):
                    kill += arr[i + k][j + l]

            # 최대값 경신
            if kill > maxKill:
                maxKill = kill

    print(f'#{tc} {maxKill}')

