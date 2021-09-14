# 포화 이진트리 / 완전 이진트리

def pre_order(n):
    if n <= last :
        print(tree[n], end=' ')  # n에서 처리할 일
        pre_order(n*2, last)
        pre_order(n*2+1, last)
def in_order(n):
    if n <= last:
        in_order(n*2, last)
        print(tree[n], end=' ')  # n에서 처리할 일
        in_order(n*2+1, last)
def post_order(n):
    if n <= last:
        post_order(n*2, last)
        print(tree[n], end=' ')  # n에서 처리할 일
        post_order(n*2+1, last)

last = 8
tree = []
