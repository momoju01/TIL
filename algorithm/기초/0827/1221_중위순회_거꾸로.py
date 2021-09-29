

def in_order(start, last):
    global cnt
    global s
    if start <= last:
        in_order(start*2, last)
        tree[start] = s[cnt]  # n에서 처리할 일
        cnt += 1
        in_order(start*2+1, last)


s = 'SOFTWARE'

tree = ['']*(len(s) + 1)
cnt = 0
in_order(1, len(s))
print(tree)