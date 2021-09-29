def f(A):
    for i in range(1, 1 << 10):  # 10개 원소 포함 여부 표시
        s = 0
        for j in range(10):
            if i & (1 << j):  # i의 j번 비트가 1이면 A[j] 원소가 부분집합에 포함
                              # 1 << j : 2^j 이므로 원소일 경우 모든 부분 집합의 개수
                s += A[j]
                if s==0:   # 부분 집합을 완성 후 확인
                    return 1
    return 0

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    print(f'#{tc} {f(arr)}')