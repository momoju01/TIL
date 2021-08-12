# 정렬
# - 주어진 리스트 중에서 최소값을 찾는다
# - 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
# - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다
# - 맨 마지막에 두 개가 남을 때까지

# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())  # 리스트 길이
#     lst = list(map(int, input().split()))
#     n_lst = [0]*10
#
#     for i in range(0, 10, 2):  # 10개 항목만 출력.
#         minIdx = 100 # 최소값
#         maxIdx = 1  # 최대값
#
#         # lst 순회하면서 최소값 최대값 찾기
#         for j in lst:
#             if j < minIdx:
#                 minIdx = j
#             if j > maxIdx:
#                 maxIdx = j
#
#         n_lst[i] = maxIdx   # i 번째에 최대값
#         n_lst[i+1] = minIdx    # i+1번째에 최소값
#
#     print(f'#{tc}', end=' ')
#     for i in range(10):
#         print(n_lst[i], end=' ')
#     print()

# 결과

#1 10 1 10 1 10 1 10 1 10 1
#2 89 8 89 8 89 8 89 8 89 8
#3 98 3 98 3 98 3 98 3 98 3


# 순서대로 정렬..

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 리스트 길이
    lst = list(map(int, input().split()))
    n_lst = [0] * 10

    # 선택정렬 : 제일 작은 것 찾으면
    for i in range(0, N-1) : # 0 -> n-2까지만 실행하면 됨
        minIdx = i
        for j in range(i+1, N):
             if lst[j] < lst[minIdx]:
                 minIdx = j
        lst[i], lst[minIdx] = lst[minIdx], lst[i]

    # 차례로 정렬하기

    for n in range(-1, -6, -1):  # 최대값 5개 큰 순으로
        n_lst[(-2) * n - 2] = lst[n]  #새로운 리스트의 짝수 인덱스에 넣기
    for n in range(5):
        n_lst[2 * n + 1] = lst[n]  #홀수 인덱스에 최소값

    print(f'#{tc}', end=' ')
    for n in n_lst:
        print(n, end=' ')
    print()