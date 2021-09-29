"""
인접 리스트
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

def bfs(s, V):
    q = [] # 큐 생성
    visited = [0]*(V+1)             # visited 생성
    q.append(s)                     # 시작점 인큐
    visited[s] = 1                  # 시작점 visited 표시

    while q:                        # 큐가 비어있지 않으면(처리할 정점이 남아 있으면)
        t = q.pop(0)                # t <- 디큐(꺼내서) # pop()으로 하면 dfs됨
        print(t)                    # t 에 대한 처리
        for i in range(1, V+1):     # t에 인접이고 미방문인 모든 i에 대해
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)         # enqueue(i)
                visited[i] = visited[t] + 1      # i visited 로 표시

def bfs2(s, V):
      q = [] # 큐 생성
    visited = [0]*(V+1)             # visited 생성
    q.append(s)                     # 시작점 인큐
    visited[s] = 1                  # 시작점 visited 표시

    while q:                        # 큐가 비어있지 않으면(처리할 정점이 남아 있으면)
        t = q.pop(0)                # t <- 디큐(꺼내서) # pop()으로 하면 dfs됨
        print(t)                    # t 에 대한 처리
        for i in range(1, V+1):     # t에 인접이고 미방문인 모든 i에 대해
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)         # enqueue(i)
                visited[i] = visited[t] + 1      # i visited 로 표시


V, E = map(int, input().split())    # 2개씩 잘라서 8번 불러오면 됨
edge = list(map(int, input().split()))
adj = [[0]*(V+1) for _ in range(V+1)]     # 인접 행렬

for i in range(E):
    n1, n2 = edge[2*i], edge[2*i + 1]  # 2의 배수로 가져오기
    adj[n1][n2] = 1
    adj[n2][n1] = 1                     # 방향이 없는 그래프 (화살표 있으면 있는 곳만 넣어줘야)


bfs(1, V)  # V: 정점 개수 정보