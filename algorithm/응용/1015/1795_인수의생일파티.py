# def dijkstra():
#
#
# 짜기
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M, X = map(int, input().split()) # N:사람 수 M:간선 수 X: 생일파티 집
#
#     INF = 987654321
#     adj1 = [[INF] * (V + 1) for _ in range(N + 1)]  # 원래 입력(진출)
#     adj2 = [[INF] * (V + 1) for _ in range(N + 1)]  # 뒤집은 입력(진입)
#
#     for _ in range(M):
#         x, y, c = map(int, input().split())
#         adj1[x][y] = c  # 단방향 그래프
#         adj2[y][x] = c  # 뒤집은 그래프
#
#     dist1 = [INF] * (N + 1)
#     dist2 = [INF] * (N + 1)
#
#     # 다익스트라 호출
#     max_value = 0
#
#
#
#     for i in range(1, N + 1):
#         if dist1[i] + dist2[i] > max_value:
#             max_value = dist1[i] + dist2[i]
#
#     print(f'{tc} {max_value}')
#
#
##### 박영준 교수님

def dijkstra(adj, D, X, N):
    # 출발지는 비용이 결정된 곳으로
    U = [0] * (N + 1)
    U[X] = 1

    # x 에서 나머지 집으로 가는 비용 초기화
    for i in range(1, N + 1):
        D[i] = adj[X][i]

    # N-1개 집의 최소 비용 결정:
    for _ in range(N-1):
        # U[w] == 0, D[w]가 최소인 w 찾기
        w = 0
        minV = INF
        for i in range(1, N + 1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i

        # w는 비용 결정 됨
        U[w] = 1
        # w에 인접인 v에 대해 D[v], D[w] + adj[w][v] 중 작은 값 선택
        for v in range(1, N +1):
            if 0 < adj[w][v] < INF:
                D[v] = min(D[v], D[w] + adj[w][v])


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split()) # N:사람 수 M:간선 수 X: 생일파티 집

    INF = 987654321
    adjM = [[INF] * (N + 1) for _ in range(N + 1)]  # 원래 입력(진출)
    adjMR = [[INF] * (N + 1) for _ in range(N + 1)]  # 원래 입력(진출)

    for i in range(1, N + 1):
        adjM[i][i] = 0
        adjMR[i][i] = 0

    for _ in range(M):
        x, y, c = map(int, input().split())
        adjM[x][y] = c
        adjMR[y][x] = c

    Din = [0] * (N + 1)
    Dout = [0] * (N + 1)

    dijkstra(adjMR, Din, X, N)
    dijkstra(adjM, Dout, X, N)  #adjm에 대해 돌리고 Dout에 넣을 거고
    # print(Din)
    # print(Dout)

    # 최대 왕복 시간
    maxV = 0
    for i in range(1, N + 1):
        if maxV < Din[i] + Dout[i]:
            maxV = Din[i] + Dout[i]

    print(f'#{tc} {maxV}')