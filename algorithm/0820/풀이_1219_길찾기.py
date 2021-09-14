#
#
# # 1. 홀짝
# # 2. 2tep
#
# # 3. 2*?  <===
# # for i in range(N):
# #     st = road[2*i]
# #     ed = road[2*i+1]
# #     print(st, ed)
#
# ########################
# # 저장 방법
# # 1. ch1, ch2 방식
# ch1 = [0] * 100
# ch2 = [0] * 100
#
# for i in range(N):
#     if ch1[road[2*i]] == 0:  # 인덱스가 시작점, 도착점이 value
#         ch1[road[2*i]] = road[2*i+1]
#     else:
#         ch2[road[2*i]] = road[2*i+1]
#
# # 2. 인접 행렬 방식
# adj_arr = [[0]*100 for _ in range(100)]
# for i in range(N):
#     adj_arr[road[2*i][road[2*i+1]] = 1


# 3. 인접 리스트

#
#
# for _ in range(10):
#     tc, N = map(int, input().split())
#     road = list(map(int, input().split()))
#
#     adj_list = [[] for _ in range(100)]
#     for i in range(N):
#         adj_list[road[2 * i]].append(road[2 * i + 1])
#
#
#     visited =[0] * 100
#     ans = 0
#
#     stack = [0]  # 시작정점 0 넣어서 초기화
#
#     while stack:    # len(stack)
#         curr = stack.pop()
#
#         if curr == 99:
#             ans = 1
#             break
#
#         # 방문하지 않았으면
#
#         # 방문했으면 건너가
#         if visited[curr]: continue
#         visited[curr] = 1
#
#         for w in adj_list[curr]:
#             if not visited[w]:
#                 stack.append(w)
#
#     print(f'#{tc} {ans}')



############################# 재귀#######################

def DFS(v):
    global ans
    if v == 99:
        ans = 1
        return

    visited[v] = 1

    for w in range(100):
        if not visited[w] and adj_arr[v][w]:
            DFS(w)   # return 걸면 안됨



for _ in range(10):
    tc, N = map(int, input().split())
    road = list(map(int, input().split()))

    adj_arr = [[0]*100 for _ in range(100)]

    for i in range(N):
        adj_arr[road[2* i]][road[2*i+1]] = 1

    visited= [0] * 100
    ans = 0

    DFS(0)
    print(f'#{tc} {ans}')