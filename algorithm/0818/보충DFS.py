# DFS : 깊이 우선 탐색 (Depth First Search)
# 자료구조 스택을 가진 DFS


# 인접했다는 걸 어떻게 표현할까??
# 1) 인접 행렬
#
# ADJ = [[0, 0, 0, 0, 0, 0, 0],  # 0
#        [0. 0, 1, 1, 0, 0, 0],
#        [0, 1, 0, 0, 1, 0, 0],
#        [0, 1, 0, 0, 1, 0, 0],
#        [0, 0, 1, 1, 0, 1, 1],
#        [0, 0, ......]

# 2) 딕셔너리로 만들 수 있음
# G = [0:[], 1:[2, 3], 2:[4], 3:[4], 4:[2, 3], 5:[4], 6:[4]]




# 3) list로
lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
visited =[False] * 8
ST = []



# v의 인접 정점 중 방문하지 않은 w를 return
# 없으면 -1 return
def findW(v):
    for i in range(0, len(lst), 2):
        if lst[i] == v and visited[lst[i+1]] == False:
            return lst[i+1]
        if lst[i+1] == v and visited[lst[i]] == False:  # 거꾸로 썼으면
            return lst[i]
    return -1

# 딕셔너리일 때
def findG(v):
    for c in G[v]:
        if visited[lst[i+1]] == False:
            return c
    return -1

# 행렬일 때
def findA(v):
    for c in range(len(ADJ[v])):
        if ADJ[v][i] == 1 and visited[i]== False:
            return lst[i]
    return -1


def dfs(v):  # v : 시작 정점
    visited[v] = True
    print(v)
    findW(v)
    ST.append(v)
    while ST:  # len(ST)랑 같음
        w = findW(v)
        if w != -1:
            ST.append(v)
            visited[w] = True
            print(w)
            v = w
        else:
            v = ST.pop(-1)




dfs(1)
