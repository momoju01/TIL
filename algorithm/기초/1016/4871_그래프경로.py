"""
유향그래프, 경로 존재: 1 없으면: 0
노드는 1번부터 존재
"""

def dfs(s, g, v):               # s: 현재 위치 g: 목적지 v:노드 개수
    stack = []                  # 스택 초기화
    visited = [0] * (v + 1)     # 1번 노드부터 존재
    n = s                       # 시작 정점을 현재 위치로
    visited[n] = 1              # 시작 정점 방문 표시

    while n > 0:                # n : 1부터 시작함 / 방문한 정점이 있으면
        # 현재 n에 인접하고 방문하지 않은 w 찾기
        for w in range(1, v + 1):
            if adjM[n][w] == 1 and visited[w] == 0:  # adjM[n][w] == n->w
                stack.append(n) # 현재 위치 경로로 저장
                n = w
                visited[n] = 1

                # 방문한 정점이 목적지인지 확인
                if n == g:
                    return 1
                #아니면 break하고 if 문 나가서 for문 다시 돌면서 다음 정점 w 찾기
                break

        # w(현재 정점에 인접하고 방문하지 않은 정점) 없으면
        else:
            if stack:           # 지나온 경로 탐색
                n = stack.pop()
            else:
                n = 0           # while문 종료
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjM = [[0]*(V+1) for _ in range(V + 1)] # 인접행렬

    for _ in range(E):
        i, j = map(int, input().split())
        adjM[i][j] = 1  # 유향 그래프이므로 한쪽 방향만 인접행렬에 담기

    S, G = map(int, input().split())  # S: 시작노드 G: 도착 노드
    ans = dfs(S, G, V)

    print(f'#{tc} {ans}')
