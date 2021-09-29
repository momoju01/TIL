# 괄호 검사랑 유사
#
# T = int(input())
#
# for tc in range(1, T+1):
#     iron_bar = input()
#
#     stack = []
#     ans = 0
#
#     for i in range(len(iron_bar))
#         if iron_bar == '(':
#             stack.append(i)
#         else:
#             # 아니면 빼기
#             stack.pop()
#             if iron_bar[i-1] == '(':
#                 # 얘는 레이저
#                     ans += len(stack)
#             else:
#                 ans += 1
#
#     print(f'#{tc} {ans}')
###############################################
# 스택 말고 카운트해서 쓸 수 있음

T = int(input())

for tc in range(1, T + 1):
    iron_bar = input()

    cnt = 0 # 막대수
    ans = 0

    for i in range(len(iron_bar))
        if iron_bar == '(':
            cnt += 1
        else:
            # 아니면 빼기
            cnt -= 1
            if iron_bar[i - 1] == '(':
                # 얘는 레이저
                ans += cnt
            else:
                ans += 1

    print(f'#{tc} {ans}')


# 쫌 변형

T = int(input())

for tc in range(1, T + 1):
    iron_bar = input()

    cnt = 0 # 막대수
    ans = 0

    for i in range(len(iron_bar))
        if iron_bar == '(':
            cnt += 1
        elif iron_bar[i - 1] == '(':
            cnt -= 1
            ans += cnt
        else:
            cnt -= 1
            ans += 1

    print(f'#{tc} {ans}')