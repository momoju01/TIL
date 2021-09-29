# SWEA_10568

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input()))
    c = [0]*10  # 0부터 9까지 c에 넣어서 셀 것

    for i in ai:
        c[i] += 1  # c에 0~9 값 추가하기

    max_idx = 0
    for i in range(1, 10):
        if c[max_idx] <= c[i]:
            max_idx = i


    print(f'#{tc} {max_idx} {c[max_idx]}')



#
# T = int(input())
# for t in range(T):
#     N = int(input())
#     cards = list(map(int, input()))
#     count = [0] * 10
#     big = 0  # 모두 같은 개수면 최대 숫자 출력하도록, 초기값에 최대값 넣어줌
#     for num in cards:
#         count[num] += 1
#         if num > big:
#             big = num
#
#     answer = big
#     max_num = count[answer]
#     for n in range(N):
#         if count[cards[n]] > max_num:  # 개수가 초기값보다 크면 경신하도록
#             answer = cards[n]
#             max_num = count[answer]
#     print(f'#{t + 1} {answer} {max_num}')