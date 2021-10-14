def find_set(x):        # find_set: x를 포함하는 집합을 찾는 연산 (대표자 반환)
    if x == p[x]:       # 자기 자신을 부모로 가리키는 원소를 찾을 때까지 탐색
        return x
    return find_set(p[x])


def union(x,y):         # x와 y를 포함하는 두 집합을 통합하는 연산
    p[find_set(y)] = find_set(x)  # y의 대표 원소가 x의 대표 원소를 가리키도록

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    p = [i for i in range(N + 1)]  # 자기 자신을 부모로 하는 만들기 (0~N)

    # 두 자리씩 끊어서 union 연산
    for i in range(0, len(arr), 2):
        union(arr[i], arr[i + 1])

    result = set()      # 부모 노드가 다를 경우 다른 조

    for i in range(1, N + 1):
        result.add(find_set(i))     # 부모 노드 넣기

    print(f'#{tc} {len(result)}')

