# 연습문제 2: 6자리 숫자에 대해서 완전 검색을 적용해서 babygin을 검사해보시오.
# 순열

# def perm(n, k):
#     if k == n:
#         print(p)
#         return
#     else:
#         for i in range(k, n):
#             p[k], p[i] = p[i], p[k]
#             perm(n, k+1)
#             p[k], p[i] = p[i], p[k]
#
# p = [1,2,3]
# perm(3, 0)

def f(n, r, i):  # n: 순열의 길이, m: 주어진 숫자 개수,  k: 결정할 위치
    if i == r:
        print(p)
    else:
        for j in range(n):  # 주어진 숫자의 개수만큼
            if u[j] == 0:   # 사용 전이면
                u[j] = 1    # 사용 표시
                p[i] = arr[j]
                f(n, r, i+1)
                u[j] = 0    # 복원

n = 5
r = 3
p = [0]*r
u = [0]*n
arr = [1, 2, 3, 4, 5]
f(n, r, 0)

