T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort()
    t.sort()

    total= 0
    # 화물이나 트럭이 남아있을 때까지
    while t and w:
        # 가장 용량이 큰 트럭에 가장 무거운 화물 실을 수 있는지 확인
        maxT = t[-1]
        maxW = w.pop()
        if maxT >= maxW:
            t.pop()  # 트럭 리스트에서 제외
            total += maxW      # 적재한 화물 무게
    print(f'#{tc} {total}')