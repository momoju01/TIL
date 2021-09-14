T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 버블소트

    for i in range(N-1):
        for j in range(N-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(f'#{tc}', end=' ')

    for a in arr:
        print(a, end=' ')
    print()