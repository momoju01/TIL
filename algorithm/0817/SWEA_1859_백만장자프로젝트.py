T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 날짜
    price = list(map(int, input().split()))
    revenue = 0
    maxI = 0
    start = 0

    while start <= N :
        maxP = 0

        # 가격이 가장 높은 날
        for i in range(maxI+1, N):
            if price[i] > maxP:
                maxP = price[i]
                maxI = i

        # 그 날 이전은 다 구매
        for i in range(start, maxI):
            revenue += maxP - price[i]
            start = maxI + 1

    print(f'#{tc} {revenue}')