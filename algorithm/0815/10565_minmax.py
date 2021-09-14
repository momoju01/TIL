T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    minV = 1000000
    maxV = 0

    for i in range(N):
        if arr[i] > maxV:
            maxV = arr[i]
        if arr[i] < minV:
            minV = arr[i]

    print(f'{tc} {maxV-minV}')

