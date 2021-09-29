T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())     # N: 화덕 크기, M: 피자 개수
    C = list(map(int, input().split()))  # 피자 당 치즈 양
    pizza = [[i, j] for i, j in enumerate(C, start=1)]  # 각 피자에 index 부여
    q = []  # 화덕

    for i in range(N):             # 화덕 크기만큼 피자 넣어주기
        q.append(pizza.pop(0))

    while len(q) != 1 :            # pizza 다 화덕에 넣고 화덕에 하나만 남을때까지 진행
        c1 = q.pop(0)              # c : q의 맨 처음 원소의 [인덱스, 치즈양]
        c1[1] //= 2
        if c1[1] != 0:             # 치즈 다 안녹은 경우
            q.append(c1)
        elif pizza:                # 치즈 다 녹았고 넣을 피자 남은 경우 화덕에 넣기
            q.append(pizza.pop(0))
    print(f'#{tc} {q[0][0]}')