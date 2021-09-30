T = int(input())

for tc in range(1, T + 1):
    N = float(input())

    i = 1
    ans = ''
    while i < 13:
        if N == 0:  # 종료 조건
            break
        if N >= 2 ** -i:  # 소수점 자리 별 포함 여부
            N -= 2 ** -i
            ans += '1'
        else:
            ans += '0'
        i += 1

    if N:
        ans = 'overflow'

    print(f'#{tc} {ans}')