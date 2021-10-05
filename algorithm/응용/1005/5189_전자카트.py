def perm(n, k):
    global minV
    if n == k:  # 4.경로 1개 완성
        s = 0
        np = [0] + p + [0]

        # 5.소요량 구하기
        for j in range(n+1): # 경유지의 출발 인덱스 기준
            s += bat[np[j]][np[j+1]]

        # 6.최소인지 확인
        if s >= minV:
            return
        elif s < minV:
            minV = s

    # 3. 순열 생성
    else:
        for i in range(n): # i: 0, 1, 2
            if u[i] == 0:  #
                u[i] = 1
                p[k] = A[i]
                perm(n, k+1)
                u[i] = 0


# 1. input
T= int(input())
for tc in range(1, T+1):
    N = int(input())
    bat = [list(map(int, input().split())) for _ in range(N)] # 배터리 소모량
    A = [0] * (N-1)  # 사무실 제외한 경유지만 저장
    u = [0] * (N-1)  # 방문 체크
    p = [0] * (N-1)  # 순열
    minV = 100 * (N+1)

    # 2. N으로 A(경유지) 생성하기 A = [1, 2, 3]
    for i in range(1,N):
        A[i-1] = i

    perm(N-1, 0)

    print(f'#{tc} {minV}')


