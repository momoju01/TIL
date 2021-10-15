"""
편의상 1번부터 N번 사람까지 번호가 붙어져 있다고 가정
서로를 알고 있는 관계일 수 있고, 아닐 수 있다.
창용 마을에 몇 개의 무리가 존재하는지 계산하는 프로그램
"""


def bfs(idx):
    q = [0] * 100
    front = rear = -1
    rear += 1  # 시작점 인큐
    q[rear] = idx
    included[idx] = 1  # 시작점 그룹에 포함 표시
    while front != rear:
        front += 1
        tmpx = q[front]
        # 인접행렬의 tmpx행 모든 열을 다 보면서, 연결은 되어있는데 아직 그룹에 포함되지 않은 사람은 큐에 넣고, included 찍기
        for c in range(1, N + 1):
            if adj_arr[tmpx][c] == 1 and included[c] == 0:
                rear += 1
                q[rear] = c
                included[c] = 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N:마을 사람 수 / M:서로를 알고 있는 사람의 관계 수
    # 좌표가 아니므로, 정점이므로, 이 사람이 그룹에 속해있는 지 아닌 지 체크/판단할 배열로 일차원
    included = [0 for _ in range(N + 1)]  # 체크 / 사람 번호를 인덱스로 사용
    # 연결관계를 나타낼 인접행렬(무방향)
    adj_arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for m in range(M):
        p1, p2 = map(int, input().split())
        adj_arr[p1][p2] = 1  # 연결되어있음을 표시
        adj_arr[p2][p1] = 1
    group = 0  # included되지 않은 사람 만나서 bfs에 들어가는 횟수
    # included 배열 앞에서부터(N번)을 for문을 돌면서 아직 그룹에 포함되어있지 않으면 bfs로 연결될 수 있는 데까지 included찍으며 연결
    for i in range(1, N + 1):  # included배열의 1번인덱스 ~ N번인덱스
        if included[i] == 0:
            group += 1
            bfs(i)

    print(f'#{tc} {group}')