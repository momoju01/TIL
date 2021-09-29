for _ in range(1, 11):
    tc = int(input())
    N = 100
    arr = [list(input()) for _ in range(N)]
    res = 1  # 회문의 길이

    for M in range(100, 0, -1):  # 회문의 길이 후보
        if res != 1:
            break
        # 행
        for i in range(N):
            if res != 1:
                break
            for j in range(N - M + 1):
                temp = 0
                for k in range(M // 2):
                    if arr[i][j + k] == arr[i][j + M - k - 1]:
                        temp += 1
                if temp == M // 2:  # 같은 단어의 수가 단어의 절반 길이와 같은지 확인
                    res = M
                    break
                # 열
                temp = 0
                for k in range(M // 2):
                    if arr[j + k][i] == arr[j + M - k - 1][i]:
                        temp += 1
                if temp == M // 2:
                    res = M

    print(f'#{tc} {res}')