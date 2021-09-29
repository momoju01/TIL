T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))  # N:부분집합 원소의 수 K:부분집합의 합
    ans = 0
    for i in range(1, 1 << 12):  # 모든 원소에 대해 부분집합 생성
        cnt = 0
        s = 0  # 부분집합의 합 저장
        for j in range(12):   # i의  j번 비트 확인
            if i & (1 << j):  # i의 j번 비트가 1이면 A[j] 원소가 부분집합에 포함
                s += A[j]   # 인덱스 j 로  리스트 A 안의 10진수 값 불러서 합에 저장
                cnt += 1      # 원소의 개수

        if cnt == N and s == K :  # 주어진 조건 만족하는지 확인
            ans += 1  # 만족하는 경우 1

    print(f'#{tc} {ans}')