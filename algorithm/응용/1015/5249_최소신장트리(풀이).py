# 1. Kruskal
def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)]  = find_set(x)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    edges = [list(map(int, input().split())) for _ in range(E)]

    edges.sort(key=lambda x : x[2])  # 2번 인덱스로 정렬하기

    # # 몰랐다면
    # edges = []
    # for _ in range(E):
    #     n1, n2, w = map(int, input().split())
    #     edges.append((w, n1, n2))
    # edges.sort()

    p = list(range(V+1))  # make_set 과정

    cnt = 0 # 간선 선택한 횟수
    ans = 0  # 가중치 더한 값
    idx = 0 # edges 인덱스

    # while cnt < V:
    #     n1 = edges[idx][0]
    #     n2 = edges[idx][1]
    #
    #     if find_set(n1) != find_set(n2):  # 대표 서로 다르다면
    #         union(n1, n2)
    #         cnt += 1
    #         ans += edges[idx][2]
    #     idx += 1

    for n1, n2, w in edges:
        if find_set(n1) != find_set(n2):
            cnt += 1
            ans += w
            union(n1, n2)
            if cnt == V: break

    print(f'#{tc} {ans}')


# 2. PRIM

def prim():
    key = [INF] * (V+1)
    visited = [0] * (V+1)

    # 선택 안 한 정점에 대해서
    for i in range(V):
        minI = -1
        minV = INF
        for i in range(V+1):
            if not visited[i] and key[i] < minV:
                minI = i
                minV = key[i]
                
        visited[minI] = 1  # 뽑았따
        # 갱신할 수 있으면 전부 갱신
        for i in range(V+1):
            if not visited[i] and adjM[minI][i] < key[i]:
                key[i] = adjM[minI][i]
    return sum(key)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    # 임의의 큰 값으로 초기값 넣어 놓기
    INF = 987654321
    adjM = [[INF] *(V+1) for _ in range(V+1)]


    for i in range(E):
        n1, n2, w = map(int, input().split())
        adjM[n1][n2] = adjM[n2][n1] = w

    print(f'{tc} {prim()}')