def prim(r, V):  # r: 시작 정점 V: 마지막 노드
    MST = [0] * (V + 1)     # MST 포함 여부
    key = [10]*(V+1)     # 가중치의 최대값 이상으로 초기화. key[v]는 MST에 속한 정점과 연결될 때의 가중치
    key[r] = 0              # 시작 정점의 key값 0으로 저장

    # 남은 정점들 MST에 포함시키기
    for _ in range(V):      # V+1개의 정점 중 V개 선택
        # MST에 포함되지 않은 정점 중(MST[u]==0), key가 최소인 u 찾기
        u = 0
        minV = 10
        for i in range(V+1):
            if MST[i] == 0 and key[i] < minV:
                u = i           # u : 최소 가중치 가진 정점
                minV = key[i]
        MST[u] = 1              # 정점 u를 MST에 추가
        # u에 인접인 v에 대해, MST에 포함되지 않은 정점이면
        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v] > 0:
                key[v] = min(key[v], adjM[u][v])  # u를 통해 MST에 포함되는 비용과 기존의 비용 비교하고 갱신
                # 최종적으로 key에는 MST에 연결되기 위한 비용들 저장됨
                # 남아있는 게 최소 비용 되면 갱신할 필요 없음

    return sum(key)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())                # V: 마지막 정점 번호 E: 간선 개수
    adjM = [[0] * (V + 1) for _ in range(V + 1)]    # 빈 인접 행렬


    for _ in range(E):                              # 엣지 개수만큼
        u, v, w = map(int, input().split())         # 간선의 양 끝 노드 u, v, 가중치 w
        adjM[u][v] = w
        adjM[v][u] = w                              # 가중치 있는 무방향 그래프

    # prim(0, V)  #0번부터 / V는 마지막 정점 번호
    print(f'#{tc} {prim(0, V)}')  # 리턴 값 : MST 가중치의 총 합