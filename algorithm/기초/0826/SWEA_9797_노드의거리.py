# def bfs(s, g):
#     q = []
#     visited = [0] * (V + 1)  # 방문 표시
#     q.append(s)
#     visited[s] = 1
#     while q:
#         t = q.pop(0)
#         if t == g:
#             return visited[t] - 1
#         for i in adjlist[t]:
#             if visited[i] == 0:
#                 q.append(i)
#                 visited[i] = visited[t] + 1
#
#     return 0
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#
#     adjlist = [[] for _ in range(V + 1)]
#
#     for i in range(E):
#         n1, n2 = map(int, input().split())
#         adjlist[n1].append(n2)
#         adjlist[n2].append(n1)
#
#     S, G = map(int, input().split())
#
#
#
#
#     print(f'#{tc} {bfs(S, G)}')



