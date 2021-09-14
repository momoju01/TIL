T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))

    minV = 10 * N  # 최소값 초기화
    min_idx = 0
    total_A = 0  # A가 모은 당근 개수 초기화

    for A in range(0, N - 1):  # 일꾼 A는 왼쪽에서부터 더해간다. 0~N-2까지만 해도 됨.
        total_A += carrot[A]
        total_B = 0  # B가 모은 당근 개수 초기화
        for B in range(N - 1, A, -1):  # 일꾼 B는 N-1부터 A+1 까지 수확
            total_B += carrot[B]

        if minV > abs(total_A - total_B):  # 절대값으로 접근
            minV = abs(total_A - total_B)
            min_idx = A

    print(f'#{tc} {min_idx + 1} {minV}')  # index가 0부터 시작이므로 1 더해준다.

