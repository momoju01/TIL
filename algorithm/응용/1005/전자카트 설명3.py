# 교수님 풀이

# 순열 만들기
def f(i, k, s):
    if i == k:  # 경로 1개 완성
        s += bat[A[k-1]][0]
        print(s)

    else:
        for j in range(i, k):
            A[i], A[j] = A[j], A[i]
            f(i+1, k, s + bat[A[i-1][A[i]]])  # 경유지가 결정될 때마다 비용 계산
            A[i], A[j] = A[j], A[i]


A = [0,1,2,3]
N = int(input())
bat = [list(map(int, input().split())) for _ in range(N)] # 배터리 소모량
f(1, 4, 0)