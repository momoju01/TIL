def f(n):
    if len(tree[n]) == 1:   # tree[n]은 다 리스트로 구성되어있어서 len 함수 쓸 수 있음
        return tree[n][0]
    else:
        if tree[n][0] == '-':
            return f(tree[n][1]) - f(tree[n][2])
        elif tree[n][0] == '+':
            return f(tree[n][1]) + f(tree[n][2])
        elif tree[n][0] == '/':
            return f(tree[n][1]) / f(tree[n][2])
        else:
            return f(tree[n][1]) * f(tree[n][2])

for tc in range(1, 11):
    N = int(input())  # 정점의 총 수
    tree = [0] * (N+1)

    for _ in range(N):
        data = input().split()
        if len(data) == 2:
            tree[int(data[0])] = [int(data[1])]  # 리스트 길이로 숫자인지 연산자인지 구별 예정이므로
        else:
            tree[int(data[0])] = [data[1]] + list(map(int, data[2:]))

    print(f'#{tc} {int(f(1))}')



