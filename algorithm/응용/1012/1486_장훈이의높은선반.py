# 민채님코드 (첫번째)
#
def inclusion():
    mn = 10000 * N
    for i in range(1 << N):
        tower = [0] * N
        for j in range(N):
            if i & (1 << j):
                tower[j] = clerks[j]  # 타워 쌓는데 필요한 직원의 키만 저장장        if sum(tower) >= B:
            if sum(tower) < mn:
                mn = sum(tower)  # 최소값 갱신
    return mn - B


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    clerks = list(map(int, input().split()))
    ans = inclusion()  # 부분집합으로 타워에 들어가는지 봄
    print(f'#{tc} {ans}')



# 민채님 코드 재귀
def includewho(cnt, s):
    global mn
    if cnt == N:
        if s >= B and s < mn:
            mn = s
        return
    else:
        if s >= mn:  # 백트래킹
            return
        includewho(cnt + 1, s + clerks[cnt])  # 포함
        includewho(cnt + 1, s)  # 미포함


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    clerks = list(map(int, input().split()))
    mn = 10000 * N
    includewho(0, 0)
    ans = mn - B
    print(f'#{tc} {ans}')