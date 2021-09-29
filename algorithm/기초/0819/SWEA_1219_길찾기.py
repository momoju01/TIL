def dfs(s, g, v):  # s: 현재 위치 g: 목적지 V: 노드 개수
    stack = []  # 스택 만들어 놓기
    visited = [0] * v
    # 시작점
    n = s  # n: 정점 위치를 현재 위치로
    visited[n] = 1

    while n != -1:
        # 현재 방문한 정점에 인접한 & 아직 방문하지 않은 w 찾기
        for w in range(v):
            if adj[n][w] == 1 and visited[w] ==0:
                stack.append(n)
                n = w
                visited[w] = 1

                # 방문한 정점에서 할 일 : 목적지인지 확인
                if n == g:
                    return 1
                break  # 끝까지 왔으면 돌아가서 아직 방문하지 않은 w 찾기
        # w 못 찾은 경우
        else:
            if stack:
                n = stack.pop()  # 지금 위치 n pop하고 이전 경로로 가서 w 찾기
            else:
                n = -1  # while문 종료

    return 0



for _ in range(10):
    tc, E = map(int, input().split())      # E = 간선 개수
    lst = list(map(int, input().split()))  # 데이터 받아오기
    S, G, V = 0, 99, 100                   # S: 시작 G: 도착 V:노드 개수
    temp = []                              # 2 개씩 끊어서 list로 받기

    # 입력받은 데이터 2 개씩 끊어서 받기
    for i in range(len(lst)):
        if i % 2 == 0:
            temp.append(lst[i:i + 2])

    # 인접행렬 담을 곳
    adj = [[0] * V for _ in range(V)]

    # temp에 있는 데이터 adj에 옮기기(있으면 1로 표기)
    for i in temp:
        adj[i[0]][i[1]] = 1


    ans = dfs(S, G, V)
    print(f'#{tc} {ans}')
