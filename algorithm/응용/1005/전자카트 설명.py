# 교수님 풀이

# 순열 만들기
def f(i, k):
    if i == k:  # 경로 1개 완성
        s = bat[0][A[0]]  # 사무실 -> 첫 경유지
        for j in range(k-1):  # 경유지의 출발 인덱스 기준
             s += bat[A[j]][A[j+1]]
        s += bat[A[k-1]][0]  # 마지막 경유지 -> 사무실

    else:
        for j in range(i, k):
            A[i], A[j] = A[j], A[i]
            f(i +1, k)
            A[i], A[j] = A[j], A[i]


A = []
N = int(input())
bat = [list(map(int, input().split())) for _ in range(N)] # 배터리 소모량
for i in range(1, N+1):  # 0부터 시작으로
    A.append(i)

f(0, 3)