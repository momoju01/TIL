# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.
# N 은 5 이상 50 이하이다.

T = int(input())

for t in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    print(f'#{t}', end=' ')

    for x in a:
        print(x, end= ' ')
    print('\n')



# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     A = list(map(int, input().split()))
#
#     for i in range(N-1, 0, -1): #구간 끝
#         for j in range(0, i): #비교할 원소 끝
#             if A[j] > A[j+1]:
#                 A[j], A[j+1] = A[j+1], A[j]
#
#     print(f'#{tc}', end=' ')
#
#     for x in A:
#         print(x, end= ' ')
#     print('\n')