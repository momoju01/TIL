"""
입력
0000000111100000011000000111100110000110000111100111100111111001100111
"""

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input()))

    print(f'#{tc}', end=' ')
    for i in range(0, len(arr), 7):
        ans = 0
        for j in range(7):
            ans += arr[i + j] * (2 ** (6 - j))  # 0번째 인덱스가 2^6 이므로
        print(ans, end=' ')
    print()

# 교수님 코드
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input()))
    ans = []
    dec = 0
    for i in range(70):  # 문제에서 70개 비트
        # i %7 0~6을 반복해서 만드는 연산
        # 1 << j j번 비트가 1인 값, 2의 j제곱수
        j = 6 - i % 7
        dec += arr[i]*(1<<j)
        if j == 0:
            ans.append(dec)
            dec = 0
    print(f'#{tc} {*ans}')


# 언용님 코드
for tc in range(1, int(input()) + 1):
    num = input()
    print(f'#{tc}', *[int(num[i:i+7], 2) for i in range(0, len(num), 7)])