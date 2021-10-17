def f(i, j):  # 시작~ 끝
    if i == j:
        return i
    else:
        l = f(i, (i+j)//2)
        r = f((i+j)//2 + 1, j)
        if arr[l] - arr[r] == -1 or arr[l] - arr[r] == 2:  # r이 이기는 경우
            return r
        else:   # 무승부일때는 번호 작은 쪽이 승리 : l이 이기는 경우
            return l


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    print(f'#{tc} {f(1, N)}')