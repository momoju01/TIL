T = int(input())

for tc in range(1, T+1) :
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))  # 충전기가 있는 정류장
    bus_stop = [0] * N  # 모든 정류장


    # 정류장에 충전기가 있는 정류장 1로 표기
    for i in charge:
        bus_stop[i] += 1

    count = 0  # 충전 횟수
    bus_pos = 0  # 버스 위치


    while True:
        # k 만큼 버스 위치 이동
        bus_pos += K
        # 범위 벗어나는 경우 (종료 조건 설정)
        if bus_pos >= N:
            break

        for i in range(bus_pos, bus_pos-K, -1):  # 버스 위치에서 K의 0번 인덱스까지 뒤로 가면서 검사
            if bus_stop[i]:  # 버스 정류장에 충전소 있다면
                count += 1
                bus_pos = i
                break  # break 해서 더 앞쪽에 충전소 있더라도 뒷쪽으로 옮겨야함

        else:  # 충전기 못 만나는 경우도 break
            count = 0  # 이전 단계에 충전해서 충전 횟수 누적되어 있더라도 0으로 출력해야함
            break

    print(f'#{tc} {count}')




