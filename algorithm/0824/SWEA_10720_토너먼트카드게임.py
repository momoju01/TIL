def f(i, j):
    # 종료조건
    if i == j:  # 한명 남은 경우는 재귀 호출 x
        return i
    else:
        r1 = f(i, (i+j)//2)
        r2 = f((i+j)//2 + 1, j)
        if lst[r1] - lst[r2] == -1 or lst[r1] - lst[r2] == 2:  # r2가 이기는 경우 -1: (1-2), (2-3)  2: (3-1)
            return r2
        else:  # 무승부일 경우는 r1이 이김
            return r1




T = int(input())
for tc in range(1, T+1):
    N =int(input())
    lst = list(map(int, input().split()))

    print(f'#{tc} {f(0, N-1)+1}')  # 인덱스라서 학생 번호는 +1
