# def inoder(node, start, last):
#     if start <= last:
#         inoder(node, 2 * start, last)
#         print(node[start], end='')
#         inoder(node, 2 * start + 1, last)
#
#
# for tc in range(1, 11):
#     N = int(input())
#     node = [0] * (N + 1)
#     for i in range(N):
#         tmp = list(map(str, input().split()))
#         node[int(tmp[0])] = tmp[1]
#     print(f'#{tc}', end=' ')
#     inoder(node, 1, N)
#     print()

def in_order(start, last):
    if start <= last:
        in_order(start*2, last)
        print(tree[start], end='')  # n에서 처리할 일
        in_order(start*2+1, last)


T = 10
for tc in range(1, T+1):
    N = int(input())    # 정점 개수이자 마지막 정점 번호
    tree = [0] * (N+1)  # 완전이진트리 only

    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]       # arr[0]: 글자 arr[1]:

    # print(tree)
    출력
    print(f'#{tc}', end=' ')
    in_order(1, N)          # 1: 시작 정점, 마지막 정점
    print()
