from collections import deque

def bfs(N, M):
    queue = deque()                     # 큐 생성
    queue.append((N, 0))                # 시작점 인큐
    visited = {}                        # 방문표시
    while queue:
        u, cnt = queue.popleft()        # dequeue
        if visited.get(u, 0): continue  # 방문한 적 없으면 방문표시
        visited[u] = 1
        if u == M: return cnt           # 연산 결과가 M과 일치하면 연산 횟수 return
        cnt += 1
        if u + 1 <= 1000000:
            queue.append((u+1, cnt))
        if 0 < u - 1:
            queue.append((u-1, cnt))
        if u * 2 <= 1000000:
            queue.append((u*2, cnt))
        if 0 < u - 10:
            queue.append((u-10, cnt))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc} {bfs(N, M)}')


#### 교수님 코드  ####
def bfs(n, m):
    v = [0] * 1000001  # 방문 기록
    q = [0] * 1000001
    front = -1
    rear = -1
    rear += 1
    q[rear] = n  # 큐에 시작 노드 인큐
    while front != rear:  # 큐가 비어있지 않으면
        front += 1
        n = q[front]  # 다음 노드를 꺼내
        if n == m:  # 찾는 노드인 경우 거리 리턴
            return v[n]
        t = [n - 10, n - 1, n + 1, n * 2]  # 인접 노드번호 계산
        for i in range(4):
            if t[i] > 0 and t[i] <= 1000000:  # 유효한 노드 번호이로
                if v[t[i]] == 0:  # 아직 방문하지 않은 노드면
                    v[t[i]] = v[n] + 1  # 거리를 기록하고
                    rear += 1
                    q[rear] = t[i]  # 큐에 추가


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    print('#{} {}'.format(tc, bfs(N, M)))