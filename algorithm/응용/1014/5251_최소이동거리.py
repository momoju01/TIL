def dijkstra(s, V):          # s: 출발 정점
    U = [0] * (V + 1)        # 비용이 결정된 정점을 1로 표시할 배열
    U[s] = 1                 # 출발점 비용 결정

    for i in range(V + 1):   # 모든 정점 v에 대해 s -> v로 가는 비용 초기값
        D[i] = adjM[s][i]

    # 남은 정점의 비용 결정
    for _ in range(V-1):     # 정점 0~V 까지였는데 1개 선택됨 : 0부터 V-1까지만

        # D[w]가 최소인 w 결정(비용이 결정되지 않은 w 중에서)
        minV = INF
        w  = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1             # 비용 결정된 정점 1로 표시

        # w->v : w에 인접한 모든 정점 v에 대해
        for v in range(V+1):
            if 0 < adjM[w][v] < INF:
                D[v] = min(D[v], D[w] + adjM[w][v])  # s-v보다 s-w-v가 비용 적으면

INF = 10 * 1000000
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())         # V: 마지막 연결지점 번호 E: 도로 개수
    adjM = [[INF]*(V+1) for _ in range(V+1)] # 노드 0부터 시작

    for i in range(V+1):                     # 자기 자신 0
        adjM[i][i] = 0

    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w                       # 유향 그래프

    D = [0] * (V+1)                          # 출발점에서 각 정점까지 최단 경로 가중치 합 저장할 배열

    dijkstra(0, V)
    print(f'#{tc} {D[-1]}')
