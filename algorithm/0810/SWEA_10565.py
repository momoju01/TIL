# SWEA 10565

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    maxV = ai[0]
    minV = ai[0]

    # 최대값 저장하기
    for i in ai:
        if maxV < i:
            maxV = i

    # 최소값 저장하기
    for i in ai:
        if minV > i:
            minV = i

    print(f'#{tc} {maxV-minV}')


# 교수님
# maxV 와 minV가 연관이 없어 보이므로 for 문 안에 if-else 문으로 써도 됨


# 정렬로 풀어도 되지만 어떤 경우보다 느림 O(n^2)
