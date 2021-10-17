# # 만들 때마다 순열 출력하기 3개 다 사용해서
#
# def f(i, N):    #P[i]의 값을 결정하는 함수
#     if i == N:  # 배열을 벗어났다 (크기와 인덱스가 일치)
#         print(P)
#     else:
#         for j in range(i, N):  # P[i] <-> P[j] 자리 교환
#             P[i], P[j] = P[j], P[i]
#             f(i+1, N)
#             P[i], P[j] = P[j], P[i]
#
# P = [1, 2, 3]
# f(0, 3)

# a[] : 데이터가 저장된 리스트
# n : 원소의 개수
# i : 현재까지 선택된 원소의 수
def perm(i, N):
    if i == N: # 하나의 순열이 생성된 경우
        print(a) # 해당 순열 출력
    else:
        for j in range(i, N):
            a[i], a[j] = a[j], a[i] # 교환을 통한 선택
            perm(i+1, N) # 선택된 원소 수를 1개 증가시키고 재귀호출
            a[i], a[j] = a[j], a[i] # 이전 상태로 복귀

a = [1, 2, 3]
perm(0, 3)
# def f2(n, r, i):  # n: 순열의 길이, m: 주어진 숫자 개수,  k: 결정할 위치
#     if i == r:
#         print(p)
#     else:
#         for j in range(n):  # 주어진 숫자의 개수만큼
#             if u[j] == 0:   # 사용 전이면
#                 u[j] = 1    # 사용 표시
#                 p[i] = arr[j]
#                 f2(n, r, i+1)
#                 u[j] = 0    # 복원
#
# # n = 5
# # r = 3
# # p = [0]*r
# # u = [0]*n
# # arr = [1, 2, 3, 4, 5]
# # f(n, r, 0)
#
#
# # 전자 카트 / 앞에 것 고정하기
# p = [0]*5
# arr = [1, 2, 3, 4, 5]
# u = [0]*5
# p[0] = arr[0]
# u[0] = 1
#
# f2(5, 5, 1)


# # 1. 반복문으로 순열 생성하기
# for i in range(1, 4):
#     for j in range(1, 4):
#         if j != i:
#             for k in range(1, 4):
#                 if k != i and k != j:
#                     print(i, j, k)

# import itertools
# mylist= [1, 2, 3]
# result = itertools.product(mylist, repeat=3)
# print(list(result))
# import itertools
# mylist = [1, 2, 3]
# result = itertools.permutations(mylist) # (mylist, 3)과 같다. r을 생략시 기본값이 리스트크기
# print(list(result))