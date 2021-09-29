"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

6
1 2 1 3 2 4 3 5 3 6
"""
def pre_order(n):
    global cnt
    if n:
        cnt += 1  # 방문한 정점의 개수를 카운트로 셈
        pre_order(left[n])
        pre_order(right[n])

# 응용
def node(n):
    if n:
        r1 = node(left[n])
        r2 = node(rignt[n])
        return r1 + r2 + 1  # 실제 정점의 개수     # 일종의 후위 순회
    else:
        return 0            # 유효한 정점 아님

# # cnt += 는 어떤 순회 하든 상관 없음... !
# def in_order(n):
#     if n:
#         in_order(left[n])
#         cnt += 1
#         in_order(right[n])
# def post_order(n):
#     if n:
#         post_order(left[n])
#         cnt += 1
#         post_order(right[n])

V = int(input())
edge = list(map(int, input().split()))
E = V - 1
left = [0] * (V+1)  # 부모 번호를 인덱스로 자식 번호 저장
right = [0] * (V+1)

for i in range(E):
    p, c = edge[2*i], edge[2*i+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

cnt = 0
pre_order(3)  # 3의 자손 수 찾기. 서브트리의 루트 제외
print(cnt)      # 3을 루트로하는 서브트리의 정점 개수
print(cnt-1)    # 3의 자손의 수

# 저장된 내용 별도로 있다면
# 정점 번호를 인덱스로하는 LIST 따로 만들기...
# node = ['', 'A', 'B', 'C', 'D']
