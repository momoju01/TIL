# # def synergy(lst):
# #     global mn
# #     cust_2 = []
# #     # cust_2의 식재료 정하기
# #     for i in range(N):
# #         if i not in lst:
# #             cust_2.append(i)
# #     # cust_1의 시너지 합
# #     syn_one = 0
# #     for a in range(len(cust_1)):
# #         for b in range(len(cust_1)):
# #             syn_one += arr[cust_1[a]][cust_1[b]]
# #     # cust_2의 시너지 합
# #     syn_two = 0
# #     for x in range(len(cust_2)):
# #         for y in range(len(cust_2)):
# #             syn_two += arr[cust_2[x]][cust_2[y]]
# #     # 차이
# #     diff = abs(syn_one - syn_two)
# #     # 최소값 갱신
# #     if diff < mn:
# #         mn = diff
# #     return
# #
# #
# # def firstcome(s, n):  # cust_1의 식재료 정하기
# #     if n == N / 2:
# #         synergy(cust_1)
# #     else:
# #         for k in range(s, N):
# #             cust_1[n] = k
# #             firstcome(k + 1, n + 1)
# #
# #
# # T = int(input())
# # for tc in range(1, T + 1):
# #     N = int(input())  # 식재료의 수
# #     arr = [list(map(int, input().split())) for _ in range(N)]
# #     cust_1 = [0] * (N // 2)
# #     mn = 99999
# #     firstcome(0, 0)
# #     print(f'#{tc} {mn}')
#
#
# def basket_combi(cnt, last):
#     global min_diff
#     if cnt == N // 2:  # 고른 인덱스의 개수가 N//2인 경우
#         # used배열 출력해보기
#         # print(used)
#         """
#         [1, 1, 0, 0]
#         [1, 0, 1, 0]
#         [1, 0, 0, 1]
#         [0, 1, 1, 0]
#         [0, 1, 0, 1]
#         [0, 0, 1, 1]
#         """
#         basket_a = []  # N은 짝수개    #basket은 combi
#         basket_b = []
#         for i in range(N):
#             if used[i] == 1:
#                 basket_a.append(i)
#             elif used[i] == 0:
#                 basket_b.append(i)
#             if basket_a and basket_b and basket_a[0] > basket_b[0]:
#                 return
#         ##프루닝 ##optional!! / 절반을 기준으로 basket_a와 basket_b간의 구성이 같은듯함
#         # if basket_a[0] > basket_b[0]:
#         #     return    ##여기 대신 위의 for문에 해줌
#
#         ####여기서 할 것은???  #중복값은 없는 순열로, 2중for문으로 인덱스 2개를 고름(S에서 i,j를 바꾸는 것도 이 순열 이중 for문에서 해결)
#         # print(basket_a, basket_b)
#         sum_synergy_a = 0
#         for idx1 in basket_a:
#             for idx2 in basket_a:
#                 # if idx1 != idx2:
#                 # print(idx1,idx2)
#                 sum_synergy_a += S[idx1][idx2]
#
#         sum_synergy_b = 0
#         for idx1 in basket_b:
#             for idx2 in basket_b:
#                 # if idx1 != idx2:
#                 # print(idx1,idx2)
#                 sum_synergy_b += S[idx1][idx2]
#         diff = abs(sum_synergy_a - sum_synergy_b)
#
#         # 여기서 구한 diff가 min_diff면 min_diff갱신
#         if diff < min_diff:
#             min_diff = diff
#
#     for idx in range(last, N):
#         if not used[idx]:
#             used[idx] = 1
#             basket_combi(cnt + 1, idx + 1)
#             used[idx] = 0
#
#
# # --------------------------------------------
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     S = [list(map(int, input().split())) for _ in range(N)]
#     # print(S)
#     """
#     [[0, 5, 3, 8],
#     [4, 0, 4, 1],
#     [2, 5, 0, 3],
#     [7, 2, 3, 0]]
#     """
#     # 1. N개를 N/2개씩 바스켓에 나눠담음(a음식을 위한 basket/ b음식을 위한 basket)
#     # 2. 바스켓 내 재료간의 순서는 상관없음 / N개 중 N/2개를 고르는 조합 생성
#
#     used = [0 for _ in range(N)]
#     min_diff = 987654321
#     basket_combi(0, 0)  # 고른 개수 cnt / last
#
#     print(f'#{tc} {min_diff}')

def nCr(n, r, s, k):  # n개에서 r개를 고르는 조합, s는 선택할 수 있는 구간의 시작, k는 고른 개수
    if k == r:
        combi.append(comb[::])  # 딥카피 해줘야 함 append 얕은 복사됨
    else:
        for i in range(s, n - r + k + 1):
            comb[k] = food[i]
            nCr(n, r, i + 1, k + 1)


def cook(A, B):
    global minV
    A_taste = 0
    for i in A:
        for j in A:
            A_taste += arr[i][j]

    B_taste = 0
    for i in B:
        for j in B:
            B_taste += arr[i][j]
    taste = abs(A_taste - B_taste)
    if taste < minV:
        minV = taste
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 999999

    food = []
    for i in range(N):
        food.append(i)

    comb = [0] * (N // 2)
    combi = []
    nCr(len(food), N // 2, 0, 0)
    for i in combi:
        A = i
        B = []
        for j in food:
            if j not in A:
                B.append(j)
        cook(A, B)

    print(f'#{tc} {minV}')



# ### 소라님#########################
def combination(arr, r):
    if r == 0:
        return [[]]
    l = []
    for i in range(len(arr)):
        m = arr[i]
        new_arr = arr[i + 1:]
        for p in combination(new_arr, r - 1):
            l.append([m] + p)
    return l
#
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     comb = combination(list(range(N)), N // 2)
#     min_gap = 999999
#
#     for a in comb:
#         b = []
#         for x in list(range(N)):
#             if x not in a:
#                 b.append(x)
#
#         cnt_a, cnt_b = 0, 0
#         # print(f'a: {a}, b: {b}')
#
#         for i in range(len(a) - 1):
#             for j in range(i + 1, len(a)):
#                 cnt_a += arr[a[i]][a[j]]
#                 cnt_a += arr[a[j]][a[i]]
#                 cnt_b += arr[b[i]][b[j]]
#                 cnt_b += arr[b[j]][b[i]]
#
#         if cnt_a >= cnt_b:
#             gap = cnt_a - cnt_b
#         else:
#             gap = cnt_b - cnt_a
#
#         if gap < min_gap:
#             min_gap = gap
# #
#     print(f'#{tc} {min_gap}')