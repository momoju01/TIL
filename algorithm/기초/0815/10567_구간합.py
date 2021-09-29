T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    maxV = 0
    minV = N * 10000

    for i in range(N-M+1):  # 전체에서 M 범위 만큼 뺀 범위 돌면서
        temp_sum = 0
        for j in range(M):  # M 영역의 합 구하기
            temp_sum += arr[i+j]

        if temp_sum > maxV:
            maxV = temp_sum
        if temp_sum < minV:
            minV = temp_sum

    print(f'#{tc} {maxV - minV}')