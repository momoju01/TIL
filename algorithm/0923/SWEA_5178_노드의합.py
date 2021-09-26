def f(n, V):
    if n > V:
        return 0
    else:
        if tree[n] > 0:    # 리프노드에 도착하면
            return tree[n] # 이미 값이 있으므로 리턴
        else:
            r1 = f(2*n, V)
            r2 = f(2*n+1, V)
            tree[n] = r1 + r2
            return tree[n]


T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())  # N: 마지막 정점, M: 리프노드 수, L: 출력할 정점
    tree = [0]*(N+1)                     # 비어있는 완전이진트리 생성

    # M개의 리프노드만큼 반복
    for _ in range(M):
        index, data = map(int, input().split())
        tree[index] = data

    f(1, N) # 순회하면서 합을 저장
    print(f'#{tc} {tree[L]}')





# def f(n, V):
#     if n > V:  # 존재하지 않는 정점인 경우 # ex 왼쪽자식만 있는 경우, 왼쪽에서는 값을 리턴하는데 오른쪽에서 None을 리턴하면, 서로 더하지 못함. 오른쪽에서는 None이 아니라 0을 리턴해줘야 값을 더할 수 있음.
#         return 0  # int와 None은 더할 수 없으므로
#     else:  # n <= V / 존재하는 정점이면 --> 1.값을 가지고 있으면 그 값을 리턴하고, 2. 0이면 더 들어가서 순회!(값이 나올 때까지)
#         if tree[n] > 0:  # 값이 있다는 것은 리프노드라는 뜻 /리프노드에 도착하면
#             return tree[n]  # 이미 값이 있으므로 더 깊이 순회할 필요 없이 리턴
#         else:
#             r1 = f(2 * n, V)  # 각각의 리턴 밸류를 받아 옴
#             r2 = f(2 * n + 1, V)
#             tree[n] = r1 + r2  # tree[n]에 값을 저장해주고 다시 올려주어야 함. 리턴
#             return tree[n]  # 루트(1)에 들어있는 값이 필요한 게 아니므로, 마지막에 노드1에 저장된 값(루트에 저장된 값)은 그냥 버릴 것
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M, L = map(int, input().split())  # N: 노드의 개수(마지막 정점), M:리프노드, L:값을 출력할 노드 번호
#     tree = [0 for _ in range(N + 1)]  # 비어있는 완전이진트리 생성
#     for m in range(M):
#         # 리프 노드 번호와 1000이하의 자연수가 주어진다.
#         leaf, value = map(int, input().split())
#         tree[leaf] = value
#         # 이 값을 채우고! 그 다음에 어쩔거냐? 순회를 하면 될 것 같음
#     # print(tree)
#
#     # 이제 탐색 시작!
#     f(1, N)  # 꼭대기서부터 탐색 시작   #여기서의 마지막 리턴 값은 버리면 됨(1노드에 있는 값을 구하라는 건 아니므로)
#     # 하고싶은 작업 ==> 순회하면서 합을 저장
#     print(f'#{tc} {tree[L]}')