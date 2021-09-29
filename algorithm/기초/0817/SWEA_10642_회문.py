T = int(input())

for T in range(1, T+1):
    tc = T
    N, M = map(int, input().split())  # N: N*N 배열 M: 회문 길이
    arr = [list(input()) for _ in range(N)]
    pal = ''

    # 행
    for i in range(N):
        for j in range(N - M + 1):
            temp = 0
            for k in range(M // 2):
                if arr[i][j+k] == arr[i][j+M-k-1]:
                    temp += 1
            if temp == M //2:   # 같은 단어의 수가 단어의 절반 길이와 같은지 확인
                for l in range(j, j+M):  # j 행부터 출력
                    pal += arr[i][l]

    # 열
    for i in range(N):  # i 가 열
        for j in range(N - M + 1):
            temp = 0
            for k in range(M // 2):
                if arr[j + k][i] == arr[j + M - k - 1][i]:
                    temp += 1
            if temp == M // 2:
                for l in range(j, j + M):
                    pal += arr[l][i]


    print(f'#{tc} {pal}')