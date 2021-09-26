def inorder(n, V):      # V = 마지막 노드
    global cnt
    if n<= V:           # 유효한 노드이면
        inorder(n*2, V)    # 왼쪽 자식으로 이동
        cnt += 1
        tree[n] = cnt         # 내가 방문한 노드에 정점 번호 쓰기
        inorder(n*2+1, V)  # 오른쪽 자식으로 이동





T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)  # 비어있는 완전 이진트리 생성
    cnt= 0
    inorder(1, N)

    print(f'#{tc} {tree[1]} {tree[N//2]}')