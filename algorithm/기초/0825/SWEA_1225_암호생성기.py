for _ in range(1, 11):
    tc = int(input())
    q = list(map(int, input().split()))
    idx = 0

    # 싸이클
    while True:
        q.append(q[0] -idx -1)
        q.pop(0)
        if q[-1] <=0 :          # 종료 조건 : 0보다 작으면 0으로
            q[-1] = 0
            break
        idx = (idx + 1) % 5  # idx 값 올려줄 때 12340 순환

    print(f'#{tc}', end=' ')
    for i in q:
        print(i, end=' ')
    print()

