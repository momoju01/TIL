# list1 구간합

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    maxV = 0
    minV = N*10000

    for i in range(N-M+1):
        temp_sum = 0
        for j in range(M):
            temp_sum += numbers[i+j]

        if maxV < temp_sum:
            maxV = temp_sum
        if minV > temp_sum:
            minV = temp_sum

    print(f'#{tc} {maxV-minV}')
#
# T = int(input())  # 테스트 케이스 T개
#
# for tc in range(1, T + 1):
#     n, m = map(int, input().split())
#     numbers = list(map(int, input().split()))
#
#     sum_max, sum_min = 0, n * 10000
#     for i in range(n - m + 1):
#         temp_sum = 0
#         for j in range(m):
#             temp_sum += numbers[i + j]
#
#         if temp_sum > sum_max:
#             sum_max = temp_sum
#
#         if temp_sum < sum_min:
#             sum_min = temp_sum
#     print(f'#{tc} {sum_max - sum_min}')