T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input())) + [0]  # 리스트 끝 0으로 해서 1로 끝날 때도 maxV랑 temp랑 비교할 수 있도록
    maxV = 0
    temp = 0
    for i in range(N+1):     # 리스트 끝에 0 더해주었으므로
        if lst[i] == 1:      # 1일 때
            temp += 1
        elif maxV < temp:  # 연속된 수 중 큰 수 비교하여 저장
            maxV = temp
            temp = 0     # temp 초기화

    print(f'#{tc} {maxV}')



###############################################################
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     lst = list(map(int, input()))
#     maxV = 0
#     temp = 0
#     for i in range(N):
#         if lst[i] == 1:  # 1일 때
#             temp += 1
#         else:  # 0일 때
#             if maxV < temp:  # 연속된 수 중 큰 수 비교하여 저장
#                 maxV = temp
#                 temp = 0  # temp 초기화
#     if maxV < temp:  # N-1인덱스에 1이 있는 경우 else문 안 돌아서 temp와 maxV 비교 못 하므로
#         maxV = temp  # for 문 빠져나온 것 저장해주기
#
#     print(f'#{tc} {maxV}')