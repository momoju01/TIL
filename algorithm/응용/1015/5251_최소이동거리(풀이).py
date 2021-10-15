def dijkstra():
    dist = [INF] *(V+1)
    visited = [0] * (V+1)
    dist[0] = 0

    for _ in range(V):
        minI = -1
        minV = INF
        for i in range(V+1):
            if not visited[i] and minV > dist[i]:
                minI = i
                minV = dist[i]
        visited[minI] = 1
        # 갱신할 수 있으면 갱신
        for i in range(V + 1):
            if not visited[i] and dist[i] > dist[minI] + adjM[minI][i]:
                dist[i] = dist[minI] + adjM[minI][i]
    return dist[V]

INF = 10 * 1000000

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())         # V: 마지막 연결지점 번호 E: 도로 개수

    adjM = [[INF]*(V+1) for _ in range(V+1)] # 노드 0부터 시작

    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w                       # 유향 그래프

    print(f'#{tc} {dijkstra()}')