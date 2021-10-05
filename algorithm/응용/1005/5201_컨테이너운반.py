T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    weights.sort()
    trucks.sort()

    cnt= 0
    while trucks and weights:
        t = trucks[-1]
        w = weights.pop()
        if t >= w:
            trucks.pop()
            cnt += w
    print(f'#{tc} {ans}')