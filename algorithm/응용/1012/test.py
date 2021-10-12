di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]


def f(i, j, k, cnt):  # k는 진행방향, cnt은 진행한 칸수
    global si, sj, maxV

    if k == 3 and i == si and j == sj:  # 출발점에 도착한 경우,
        if maxV < cnt:
            maxV = cnt
            return
    elif i < 0 or i >= N or j < 0 or j >= N:  # 범위를 벗어난 경우, 리턴
        return

    elif arr[i][j] in tour_list:  # 숫자가 중복된 경우
        return

    else:
        tour_list.append(arr[i][j])
        if k == 0 or k == 1:  # 오른쪽 방향 그대로 가거나 왼쪽으로 꺾었을 경우에
            f(i + di[k], j + dj[k], k, cnt + 1)  # K 방향으로 가보고, 막히면 다음방향으로 바꿈
            f(i + di[k + 1], j + dj[k + 1], k + 1, cnt + 1)  # K가 0이였으면 1로, 1이였으면 2로 바꿔서 진행
        elif k == 2:
            if i + j != si + sj:  # 같지 않다는 건, 출발점과 같은 대각선에 없다는 것. 계속 직진
                f(i + di[2], j + dj[2], k, cnt + 1)
            else:  # 같다는 건 출발점과 같은 대각선에 있다는 것, 오른쪽 위 방향으로 직진
                f(i + di[3], j + dj[3], k + 1, cnt + 1)
        else:  # K = 3이면, 계속 직진
            f(i + di[3], j + dj[3], k, cnt + 1)

        tour_list.remove(arr[i][j])  # else 구문의 조건문절에서 나온 경우, 리스트 마지막 항 제거해서 원상복귀


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = -1
    tour_list = []
    for i in range(N):
        for j in range(1, N - 1):
            si = i
            sj = j
            tour_list.append(arr[i][j])
            f(i + 1, j + 1, 0, 1)
            tour_list.remove(arr[i][j])

    print(f'#{tc} {maxV}')