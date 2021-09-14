def dfs(s, g, v):  # s: 현재 위치 g: 목적지 V: 노드 개수
    stack = []  # 스택 만들어 놓기
    visited = [0] * (v+1)
    # 시작점
    n = s  # n: 정점 위치를 현재 위치로
    visited[n] = 1

    while n > 0: # 방문한 정점이 있으면
        # 현재 방문한 정점에 인접한 & 아직 방문하지 않은 w 찾기
        for w in range(1, v+1):
            if adj[n][w] == 1 and visited[w] ==0:
                stack.append(n)
                n = w
                visited[n] = 1

                # 방문한 정점에서 할 일 : 목적지인지 확인
                if n == g:
                    return 1
                break  # 끝까지 왔으면 돌아가서 아직 방문하지 않은 w 찾기
        # w 못 찾은 경우
        else:
            if stack:
                n = stack.pop()  # 지금 위치 n pop하고 이전 경로로 가서 w 찾기
            else:
                n = 0  # while문 종료

    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V: 노드 개수, E = 간선 개수
    adj = [[0]*(V+1) for _ in range(V+1)]  # 인접행렬 담을 곳

    for _ in range(E):  # 간선의 개수만큼 반복
        n1, n2 = map(int, input().split())  # n1 n2 순으로 입력되는 데이터 받아서
        adj[n1][n2] = 1  # 인접행렬에 담기
        # adj[n2][n1] = 1  # 양방향일 경우 반대편도 추가

    S, G = map(int, input().split())  # S: 시작 G: 도착
    ans = dfs(S, G, V)
    print(f'#{tc} {ans}')