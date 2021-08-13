def search(start):  # 도착지에서 위로 올라가는 함수
    i = 99  # 행
    j = start  # 열
    while i > 0 :  # 맨 윗줄에 도착하기 전까지 위로 올라감
        i -= 1   # 위로 한 칸 이동
        # 왼쪽 칸이 1이면
        if j>0 and ladder[i][j-1]:  # 왼쪽 칸이 1이면
            while j > 0 and ladder[i][j-1] != 0:  # 0을 만날 때까지 이동
                j -= 1
        # 오른쪽 칸이 1이면
        elif j<99 and ladder[i][j+1] == 0:  # 오른쪽 칸이 1이면
            while j < 99 and ladder[i][j+1] != 0:
                j += 1
        # 좌우가 0이면
        else:
            i -= 1

    return j  # 0번 행에 도착했을 때의 열(출발지) 리턴


T = 10
for tc in range(1, T+1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]