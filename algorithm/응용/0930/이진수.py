# # 성한 님 코드
# list_16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
# T = int(input())
# for test in range(1, T + 1):
#     N, s16 = input().split()
#     N = int(N)
#     deci_list = [0] * N
#
#     for i in range(N):
#         for k in range(16):
#             if list_16[k] == s16[i]:
#                 deci_list[i] = k
#
#     print('#{}'.format(test), end=' ')
#
#     for j in range(N):
#         output = ''
#         for l in range(3, -1, -1):
#             output += '1' if deci_list[j] & (1 << l) else '0'
#         print(output, end='')
#
#     print()
#
#
# # 태균 님 코드
# for tc in range(int(input())):
#     N, hex = input().split()
#     result = ''
#
#     for i in range(int(N)):
#         temp = str(bin(int(hex[i], 16)))
#         a = len(temp[2:])
#         while a < 4:
#             a += 1
#             result += '0'
#         result += temp[2:]
#
#     print(f'#{tc + 1} {result}')
#
#
#
# # 민채 님 코드
# T = int(input())
# for t in range(1, T+1):
#     N, hexa = input().split()
#     N = int(N)
#     ans = ''
#     for h in hexa:
#         num = int(h, 16)
#         for j in range(3, -1, -1):
#             if num & (1 << j):
#                 ans += '1'
#             else:
#                 ans += '0'
#     print(f'#{t} {ans}')
#

T = int(input())
for tc in range(1, T + 1):
    N, hexa = input().split()  # 문자열로 받기
    result = ''

    for i in range(int(N)):
        num = int(hexa[i], 16)
        for j in range(3, -1, -1):
            result += '1' if num & (1<<j) else '0'

    print(f'#{tc} {result}')