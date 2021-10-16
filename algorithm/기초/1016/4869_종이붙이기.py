T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    n = N // 10

    ans = [0] * (n + 1)  # 0부터 시작

    ans[0] = 1
    ans[1] = 1

    for i in range(2, n + 1):
        ans[i] = ans[i-1] + ans[i-2] * 2

    print(f'#{tc} {ans[n]}')
