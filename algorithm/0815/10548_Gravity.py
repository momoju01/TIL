# 방의 가로 길이  N

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = 0  # 최대 낙차 값

    #개별 i마다 낙차 세기
    for i in range(N-1):  # N-1의 낙차 = 0
        count = 0  # 개별 i마다 낙차 계산해야 하므로 for문 안에 위치
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                count += 1

        # 낙차 계산 끝나면 i의 낙차끼리 비교.
        if maxV < count:
            maxV = count

    #test case 별로 max 값 출력
    print(f'#{tc} {maxV}')