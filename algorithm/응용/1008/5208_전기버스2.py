

# idx: 현재 내가 있는 버스 정류장 번호
# e: 잔여 배터리
# c: 지금까지의 교환 횟수

def move(idx, e, c):
    global ans
    if idx == bus_stop[0]:
        # 교환횟수 비교해주기
        if ans > c:
            ans = c
    else:
        if e > 0:  # 배터리 방전 되지 않았을 때만
        # 배터리 교체하지 않고 내려보내기 ~~
        move(idx+1, e-1, c)
        # 배터리를 교체하고 내려보내기
        if c < ans:  # 교환 횟수 작을때만 내려보내기
            move(idx+1, bus_stop[idx]-1, c+1)

T = int(input())
for tc in range(1, T+1):
    bus_stop = list(map(int, input().split()))  # 0번 인덱스:정류장 수,  1~ : 해당 번호의 정류장에 있는 충전지 수
    ans = 987654321

    move(2, bus_stop[1]-1, 0)
    print(f'#{tc} {ans}')