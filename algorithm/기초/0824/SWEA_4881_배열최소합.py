# 만들 때마다 순열 출력하기 3개 다 사용해서

def f(i, N, s):    # i: 고려할 원소 s:고려한 구간의 합
    global min_sum
    if i == N:  # 배열 벗어난 경우(완료한 경우)
        if min_sum > s:
            min_sum = s
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            f(i+1, N, s + arr[i][P[i]])  # 기존값에 더한 값으로 재귀함수 호출
            P[i], P[j] = P[j], P[i]  # 원상복구


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 9 * N
    P = list(range(N))
    f(0, N, 0)
    print(f'#{tc} {min_sum}')
