T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    bus_stop = [0] * N

    # 충전기가 있는 정류장에 1로 표시
    for i in charge:
        bus_stop[i] += 1

    count = 0  # 충전 횟수
    bus_pos = 0  # 버스 위치

    while True:
        bus_pos += K  # 버스의 위치 K만큼 이동

        if bus_pos >= N:  # 종료 조건 설정
            break
        for i in range(bus_pos, bus_pos-K, -1):  # 버스 위치에서 백스탭으로 정거장 있는지 확인
            if bus_stop[i]:  # 충전소 있다면 버스 위치 옮김
                count += 1
                bus_pos = i
                break
        else:
            count = 0
            break

    print(f'#{tc} {count}')
