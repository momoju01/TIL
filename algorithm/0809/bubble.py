T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    #버블 정렬...
    '''
    for i : n-1 -> 0 #구간 끝
        for j : 0 -> i-1 # 비교할 왼쪽 원소
            if A[j] > A[j+1]
                A[j] <-> A[j+1]
    A의 원소 출력
    # '''
    # # 무식한 방법
    # print(f'#{tc}', end=' ')
    # for x in A:
    #     print(x, end= ' ')

    for i in range(N-1, 0, -1): #구간 끝
        for j in range(0, i): #비교할 원소 끝
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

    print(f'#{tc}', end=' ')

    for x in A:
        print(x, end= ' ')
    print('\n')