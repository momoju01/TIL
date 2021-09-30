T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    S = ''
    for i in range(N):  # 마지막 N개 비트 역순으로 저장됨
        if M & (1 << i):
            S += '1'
        else:
            S += '0'
    res = 'ON'

    for i in range(len(S)):
        if S[i] == '0':
            res = 'OFF'
            break
    print(f'#{tc} {res}')