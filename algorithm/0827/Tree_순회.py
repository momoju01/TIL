"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

6
1 2 1 3 2 4 3 5 3 6
"""
def pre_order(n):
    if n:
        print(n, end=' ')        # n에서 처리할 일
        pre_order(left[n])
        pre_order(right[n])
def in_order(n):
    if n:
        in_order(left[n])
        print(n, end=' ')  # n에서 처리할 일
        in_order(right[n])
def post_order(n):
    if n:
        post_order(left[n])
        print(n, end=' ')  # n에서 처리할 일
        post_order(right[n])

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

pre_order(1)
print()
in_order(1)
print()
post_order(1)


# 저장된 내용 별도로 있다면
# 정점 번호를 인덱스로하는 LIST 따로 만들기...
node = ['', 'A', 'B', 'C', 'D']
