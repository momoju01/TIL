'''
마지막 정점 번호, 간선 수
6 8
0 1 0 2 0 5 0 6 4 3 5 3 5 4 6 4
'''

V, E = map(int, input().split())
edge = list(map(int, input().split()))

# 인접 행렬로 저장
adjM = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]   # 두 개씩 끊어서 읽어오기
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1  # 무향 그래프


# 인접 리스트로 저장
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)  # 무향그래프 [[1, 2, 5, 6], [0], [0], [4, 5], [3, 5, 6], [0, 3, 4], [0, 4]]
                         # 유향그래프프 [1, 2, 5, 6], [], [], [], [3], [3, 4], [4]]

print(adjL)