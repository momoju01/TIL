# 교수님 풀이

# 순열 만들기
def f(i, k):
    if i == k:  # 경로 1개 완성
        s = 0
        for j in range(k-1):  # 경유지의 출발 인덱스 기준
            s += bat[A[j]][A[j+1]]
        s += bat[A[k-1]][0]  # 마지막 경유지 -> 사무실
        print(s)
    else:
        for j in range(i, k):
            A[i], A[j] = A[j], A[i]
            f(i+1, k)
            A[i], A[j] = A[j], A[i]


A = [0,1,2,3]
N = int(input())
bat = [list(map(int, input().split())) for _ in range(N)] # 배터리 소모량
f(1, 4)