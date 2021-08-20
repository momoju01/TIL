# 사야하나, 팔아야 하나?
# 나를 기준으로 최대값 가져오기
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cost = list(map(int, input().split()))  # 가격들 입력 받기
#
#     ans = 0
#
#     for i in range(N-1):  # 어차피 마지막 날 사는 의미 x
#         max_cost = cost[i]
#
#         for j in range(i+1, N):  # 끝까지 보겠다.
#             if max_cost < cost[j]:
#                 max_cost = cost[j]
#
#         if max_cost > cost[i]:
#             ans += max_cost - cost[i]
#
#     print(f'{tc} {ans}')
#
####################################################################

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     cost = list(map(int, input().split()))  # 가격들 입력 받기
#
#     ans = 0
#
#     is_sell = [False] * N
#
#     for i in range(N-1):
#         for j in range(i+1, N):
#             if cost[i] < cost[j]:
#                 is_sell[i] = True
#                 break
#
#     buy_cost = 0
#     buy_cnt = 0
#
#     for i in range(N):
#         if is_sell[i]:
#             buy_cost += cost[i]
#             buy_cnt += 1
#         else:
#             ans += (cost[i*buy_cnt) - buy_cost
#             buy_cost = 0
#             buy_cnt = 0
#
#     print(f'#{tc} {ans}')
########################################################################

# 3. 반대로 생각해보자
T = int(input())

for tc in range(1, T+1):
    N = int(input())  # N: 날짜 수
    cost = list(map(int, input().split()))  # 각 날의 매매가
    max_cost = cost[-1]  # 가장 최근 날짜의 가격을 최대값으로 설정
    ans = 0

    # 뒤에서 세는 방식
    for i in range(N-2, -1, -1):
        if cost[i] < max_cost :  #직전 날 가격이 최대값보다 작으면 수익발생
            ans += max_cost - cost[i]
        else:  # 가격이 같거나 크면 새로운 최대값으로 설정
            max_cost = cost[i]

    print(f'#{tc} {ans}')


