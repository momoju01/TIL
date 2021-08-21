T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    maxV = lst[0]
    maxI = 0

    for i in range(1, N):
        if lst[i] > maxV:
            maxV = lst[i]
            maxI = i

    print(f'#{tc} {maxI+1} {maxV}')
