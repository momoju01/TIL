T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    while M:
        q.append(q[0])
        q.pop(0)
        M -= 1
    print(f'#{tc} {q[0]}')