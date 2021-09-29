# 입력 받을 것 많으니 주의
# T, N, *A, *B, P, *C

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 버스 노선 개수

    bus_stop = [0] * 5001 # 전체 버스 정류장

    # A, B 각각 들어올 때마다 처리해주기
    for _ in range(N):
        A, B = map(int, input().split())
        # A이상 B이하 (A, B 모두 포함)
        for i in range(A, B+1):
            bus_stop[i] += 1


    print(f'#{tc}', end =' ')
    P = int(input())
    for i in range(P):
        C = int(input())
        print(bus_stop[C], end=' ')
    print()