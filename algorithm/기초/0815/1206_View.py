# 좌우 두 칸 비교

for tc in range(10):
    N = int(input())
    arr = list(map(int, input().split()))

    res = 0

    for i in range(2, N-2):

        temp = arr[i-2]
        if temp < arr[i-1]:
            temp = arr[i-1]
        if temp < arr[i+1]:
            temp = arr[i+1]
        if temp < arr[i+2]:
            temp = arr[i+2]

        if arr[i] - temp > 0:
            res += arr[i] - temp

    print(f'#{tc+1} {res}')

