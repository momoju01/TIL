T =int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    start = 1
    end = P
    cntA = 0
    cntB = 0
    winner = '0' # 비기면 0
    
    # A 탐색 소요 시간
    while start <= end:
        c = (start + end)//2
        cntA += 1
        # A의 경우
        if c == A:  # 검색 완료
            break
        elif c > A:  # A가 왼쪽에 있으면(중위값이 목표값보다 크면)
            end = c
        else:
            start = c
    
    # B 탐색 소요 시간
    start = 1
    end = P
    while start <= end:
        c = (start + end) // 2
        cntB += 1
        # B의 경우
        if c == B:  # 검색 완료
            break
        elif c > B:  # B가 왼쪽에 있으면(중위값이 목표값보다 크면)
            end = c
        else:
            start = c

    if cntA > cntB:
        winner = 'B'
    elif cntA < cntB:
        winner = 'A'
    print(f'#{tc} {winner}')

