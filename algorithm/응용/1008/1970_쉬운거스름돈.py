T = int(input())
for tc in range(1, T+1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0] * 8
    for i in range(8):
        if N == 0:
            break
        if N//money[i] > 0:
           cnt[i] = N//money[i]
           N -= cnt[i] * money[i]


    print(f'#{tc}')
    for i in cnt:
        print(i, end=' ')
    print()