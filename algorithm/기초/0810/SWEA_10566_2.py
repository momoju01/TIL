T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = [0] + list(map(int, input().split())) + [N]

    ans = 0
    last = 0 # 마지막 충전 위치

    # 마지막 충전 위치를 저장하는 방법
    for i in range(1, M+2):
        if charge[i]-charge[i-1] > K:  # 운행 불가 간격인지 확인
            ans = 0
            break
        if charge[i] > last + K:  # 마지막 충전 위치로부터 현재 정류장에 올 수 없으면
            last = charge[i-1]
            ans += 1

    print(f'#{tc} {ans}')