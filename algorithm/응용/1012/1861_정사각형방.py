def dfs(x, y, c):
    global mx, ans
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 위, 오, 아래, 왼
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == arr[x][y] + 1:
            dfs(nx, ny, c + 1)
    else:  # 탐색 불가하면
        if c > mx:
            mx = c
            ans = start
        elif c == mx:
            if start < ans:  #
                ans = start
        return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    ans = 10 ** 3
    for i in range(N):
        for j in range(N):
            if N ** 2 - arr[i][j] < mx:  # 찾은 길이가 남은 길이보다 길면 찾을 필요 x
                continue
            start = arr[i][j]
            dfs(i, j, 1)
    print(f'#{tc} {ans} {mx}')



# 민형님 코드(교수님 설명)
def check(x, y):
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if arr[ny][nx] - arr[y][x] == 1:
                return True
    return False


d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * (n * n + 1)
    for i in range(n):
        for j in range(n):
            if check(j, i):
                visited[arr[i][j]] = 1

    room, res = 0, 0
    num = 1
    tmp = 0
    while num < n * n:  # cnt 배열 세기
        if visited[num]:
            tmp = num
            while visited[tmp]:
                tmp += 1
            tmp -= num
            if tmp + 1 > res:
                room, res = num, tmp + 1
            num += tmp + 1
        else:
            tmp = 0
            num += 1

    print(f'#{tc} {room} {res}')


## 채현님 코드 (보충)
#visit이라는 counting배열을 이용! - input에 중복된 숫자가 없어서 가능
#문제 - N^2개의 방이 N×N형태로 늘어서 있다. / 이 숫자는 모든 방에 대해 서로 다르다.
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    visit = [0 for _ in range(N*N+1)] #방번호를 인덱스로 쓸 것
    """
    [[1, 2], [3, 4]]
    [[9, 3, 4], [6, 1, 5], [7, 8, 2]]
    """
    #1. 받은 arr를 행우선탐색하면서 각 셀에서 상하좌우를 보며 이동할 수 있는 방(현재 셀의 숫자 +1의 값을 가진 셀이 존재한다면 visit배열에 1을 찍어두기)
    for i in range(N):
        for j in range(N):
            ##각 arr[i][j]셀에 접근가능한 상태.
            #상하좌우에 있는 다른 방으로 갈 수 있음.
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0<=ni<N and 0<=nj<N and arr[ni][nj] == arr[i][j] + 1:
                    #다음에 갈 수 있는 방이 있으면 visit의 지금 arr[i][j]방번호에 1표시
                    visit[arr[i][j]] = 1
    # print(visit)
    """
     0  1  2  3  4  5  6  7  8  9
    [0, 1, 0, 1, 0]                 #len: 5
    [0, 0, 0, 1, 1, 0, 1, 1, 0, 0]  #len: 10
    """
    #2. 완성된 visit 카운팅배열을 뒤에서 탐색하면서(같은최대값을 가지면, 앞의 인덱스로 자동갱신되도록, max방개수 판단 시 =를 넣어줌.
    #이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력
    departR = 0 #visit의 0인덱스는 1이 찍힐 일이 없으니! 초기값으로 써도 괜찮을 것
    maxCnt = 0
    #처음에 출발해야 하는 방 번호와 최대 몇 개의 방을 이동할 수 있는지를 공백으로 구분하여 출력
    for i in range(len(visit)-1, -1, -1):
        # print(i)  #4 3 2 1 0
        # 뒤에서부터 쭉 봐오다가 1이 있으면
        if visit[i] == 1:
            tmp_one_cnt = 2 #선언&초기값. #+1  #i에서 1이 걸렸으면, 'i에서 다음방에 갈 수 있어서'visit의 i자리에 1이 있었던 것이므로, 다음 방까지 갈 수 있는 것으로 카운팅 / 여기 맞춰서 departR계산할 때도 tmp_one_cnt로 많이 빼진 것 다시 +2해서 맞춰주기.
            j = i-1
            while j>0 and visit[j] == 1:  #visit배열 나가지 않을 때까지(0인덱스는 고려하지 않으므로, 등호는 제외해도 될 것)
                # if visit[j] == 1: #0인데도 j계속도는것 막기 위함 / 이 조건을 애초에 while실행조건으로 옮겨넣기
                tmp_one_cnt += 1
                j-=1
            #while을 돌고 나왔는데, maxCnt보다 '같거나'크면, departR을 바꿔줌('같거나'로 등호를 넣으면 이동할 수 있는 방의 개수가 최대인 방이 여럿인 경우, 가장 방넘버가 작은 방이 departR에 갱신되어 저장될 것)
            if tmp_one_cnt >= maxCnt:
                departR = i-tmp_one_cnt+2 #i에 걸려서 if문으로 들어왔으므로
                maxCnt = tmp_one_cnt
    print(f'#{tc} {departR} {maxCnt}')