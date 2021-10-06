T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = []
    for _ in range(N):
        start, end = map(int, input().split())
        A.append((start, end))  # 시작과 종료 시간 묶어서 저장하기

    # 종료시간 빠른 순으로 정렬
    for i in range(0, N - 1):
        minI = i
        for j in range(i + 1, N):
            if A[j][1] < A[minI][1]:  # 종료시간 비교
                minI = j
        A[i], A[minI] = A[minI], A[i]

    S = [A[0]]  # 선택된 활동들의 집합 넣을 list #첫 번째 활동은 무조건 추가

    j = 0    # 선택한 활동(1)의 직전 활동 나타내는 인덱스

    for i in range(1, N): # 두 번째 활동부터
        if A[i][0] >= S[j][1]:    # j 종료 시간 이후에 시작하는 활동 찾기
            S.append(A[i])
            j+=1

    print(f'#{tc} {j+1}')  # +1 :첫 번째 활동 count 해주기