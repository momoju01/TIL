# 1. bfs로 풀 수도 있음
def bfs(st):
    Q = [st]
    team[st] = 1
    while Q:
        p = Q.pop(0)
        for i in range(1, N+1):
            if not team[i] and adjM[p][i]:
                team[i] = 1
                Q.append(i)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N:사람 수 M:신청서 수

    edges = list(map(int, input().split()))  # 신청서 한 줄로 들어옴

    adjM = [[0]*(N+1) for _ in range(N+1)]

    # for i in range(0, len(edges), 2):

    for i in range(M):
        a = edges[i*2]
        b = edges[i*2 + 1]

        adjM[a][b] = adjM[b][a] = 1  # 무향그래프

    ans = 0
    team = [0] *(N+1)

    for i in range(1, N+1):
        if not team[i]:
            ans += 1
            bfs(i)

    print(f'#{tc} {ans}')


### 2. 상호 배타 집합  ####################################################

def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N:사람 수 M:신청서 수

    edges = list(map(int, input().split()))  # 신청서 한 줄로 들어옴
    p =[i for i in range(N + 1)]  # 대표 원소 자기자신으로 초기화
    # p = list(range(N+1))

    for i in range(M):
        a = edges[2*i]
        b = edges[2*i + 1]

        p[find_set(b)] = find_set(a)  # b의 대표를 a의 대표로 하겠다.

    ans = 0
    for i in range(1, N + 1):
        if p[i] == i:
            ans += 1
    print(f'#{tc} {ans}')