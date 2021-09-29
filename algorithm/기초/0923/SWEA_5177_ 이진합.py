# enqueue
def enq(data):
    global last
    last += 1           # 완전이진트리 유지(마지막 정점 추가)
    tree[last] = data
    c = last            # 새 정점을 자식으로
    p = c//2
    while p > 0 and tree[p] > tree[c]:       # 부모가 존재하고, 최소 힙 규칙에 어긋나면
        tree[p], tree[c] = tree[c], tree[p]  # 교환
        c = p                                # 부모를 새로운 자식으로해서 규칙 확인하는 것
        p = c //2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N+1)  # 마지막으로 라스트가 되는 애까지
    last = 0            # 힙의 마지막 정점 번호

    for x in arr:
        enq(x)


    # 마지막 노드의 조상 노드의 합
    # 자식 노드의 인덱스 c : N+1
    # 부모 노드의 인덱스 p : c // 2

    cnt = 0
    p = last // 2
    while p > 0:
        cnt += tree[p]
        p //= 2

    print(f'#{tc} {cnt}')