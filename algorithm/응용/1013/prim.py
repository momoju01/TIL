'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
#
#
# def prim(start, V):  # MST 가중치의 합을리턴하
#     key =[INF] * (V+1)  # KEY[i] i가 MST
#     key[start] = -
#     MST = [0] * (V + 1)
#     pi = [0] * (V + 1)
#     for _ in range(V):  # 모든 정점이 MST에 포함될 때까지
#         # MST에 포함되지 않은 정점 중 key[u]가 최소인 u 찾기
#         u = 0
#         minV = INF
#         for i in range(1, V + 1):
#             if MST[i] == 0:
#                 if key[i] < minV:
#                     u = i
#                     minV = key[i]
#         MST[u] = 1  # key[u]가 최소인 u를 MST에 추가
#         for v in range(V + 1):  # u에 인접인 v에 대해
#             if MST[v] == 0 and adj[u][v] != 0:
#                 if key[v] > adj[u][v]:

def prim1(r, V):
    MST = [0]*(V+1)       # MST 포함 여부
    key = [10000]*(V+1)   # 가중치의 최대값 이상으로 초기화. key[v]는 MST에 속한 정점과 연결될 때의 가중치
    key[r] = 0            # 시작 정점의 key
    for _ in range(V):    # V+1 개의 정점 중 V 개 선택
        # MST에 포함되지 않은 점정 중(MST[U]==0), key가 최소인 u 찾기
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
        MST[u] = 1        # 정점 u를 MST에 추가
        # u에 인접인 v에 대해, MST에 포함되지 않은 정점이면
        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v] > 0:
                key[v] = min(key[v], adjM[u][v])  # u를 통해 MST에 포함되는 비용과 기존의 비용 비교하고 갱신
                # 최종적으로 key에는 MST에 연결되기 위한 비용들 저장됨
                # 남아있는 게 최소 비용 되면 갱신할 필요 없음

    return sum(key)       # MST 가중치의 합


def prim2(r, V):
    MST = [0]* (V+1)
    MST[r] = 1
    s = 0
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):  # MST에 포함된 정점i와 인접한 정점j 중 MST에 포함되지 않고 가중치가 최소인 정점u 찾기
            if MST[i] == 1:
                for j in range(V+1):
                    if adjM[i][j] > 0 and MST[j]==0 and minV > adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1
    return s
        # MST에 포함된 정점과 인접한 정점 중 가중치가 최소인 정점 u 찾기



V, E = map(int, input().split())
adjM = [[0]* (V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w  # 가중치가 있는 무방향 그래프

    adjL[u].append((v, w))  # 인접리스트일 때
    adjL[v].append((u, w))
    """
    [[(1, 32), (2, 31), (5, 60), (6, 51)], [(0, 32), (2, 21)], [(0, 31), (1, 21), (4, 46), (6, 25)], [(4, 34), (5, 18)], [(2, 46), (3, 34), (5, 40), (6, 51)], [(0, 60), (3, 18), (4, 40)], [(0, 51), (2, 25), (4, 51)]]
    """

# print(adjM)
# print(adjL)
# print(prim1(0, V))
print(prim2(0, V))
