T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 9
    boxes = list(map(int, input().split()))  # 0~8

    maxV = 0  # 가장 큰 낙차 값 초기화

    for i in range(N-1):  # N-1번째 인덱스일 때 낙차 0이므로 0 -> N-2 까지
        count = 0
        for j in range(i+1, N):  # i의 오른쪽 값만 비교
            if boxes[i] > boxes[j]:
                count += 1
        if maxV < count:
            maxV = count   # count값 maxV에 업데이트 하고 i+1로

    print(f'#{tc} {maxV}')