# dikstra 로 풀기
# 0번부터 시작!!

"""
V E
u v w(비용)

5 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
"""

def dijkstra(s, V):     # s: 출발 정점
    U = [0] * (V + 1)   # 비용이 결정된 정점을 표시
    U[s] = 1            # 출발점 비용 결정

    for i in range(V + 1):
        D[i] = adjM[s][i]  # 출발 정점 행을 고스란히 복사해오면 d의 초기 비용 결정됨


    # 남은 정점의 비용 결정
    # 0 번부터 시작했기 때문에 V + 1개까지 있는 것임
    # 나머지 V 번 돌면 됨
    for _ in range(V):  # 남은 정점 개수만큼 반복
        # D[w]가 최소인 w를 결정, w는 비용이 결정되지 않은 정점w 중에서 (교재에 수학적 표현 보기)
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1  # 비용 결정

        for v in range(V+1):
            if 0 < adjM[w][v] < INF:
                D[v] = min(D[v], D[w] + adjM[w][v])


INF = 10000
V, E = map(int, input().split())
adjM = [[INF]*(V + 1) for _ in range(V + 1)]

for i in range(V + 1):  #자기 자신은 0
    adjM[i][i] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w      # 유향

D = [0] * (V + 1)
dijkstra(0, V)
print(D)