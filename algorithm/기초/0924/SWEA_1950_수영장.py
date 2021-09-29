def f(n, s):        # n월, s 이전까지의 비용
    global minV
    if n > 12:      # 모든 달에 대한 고려가 끝났으면
        if minV > s:
            minV = s
    # elif minV < s:
    #     return
    else:
        # # 1일권과 한달 권 나눠서 할 경우
        # f(n+1, s + swim[n]*price[0])  # 1일권 결제
        # if swim[n]:                   # 이용일 있는 경우 한달치 결제
        #     f(n+1, s + price[1])

        f(n+1, s + min(swim[n]*price[0], price[1]))  # 1개월만 결제하는 경우
        f(n+3, s + price[2])                         # n월에 3개월 이용권을 결제하는 경우


T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    swim = [0] + list(map(int, input().split()))  # 1~12월을 인덱스로 사용
    minV = price[3]
    f(1,0)
    minV = min(minV, price[3])  # 1년권과 비교

    print(f'#{tc} {minV}')