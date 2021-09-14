for tc in range(1, 11):
    N = int(input())
    H = list(map(int, input().split()))
    result = 0  # 전체 조망권 확보된 세대 수

    for i in range(2, N-2):  # 조망권 고려할 칸 i를 좌우 2칸과 비교
        maxV = H[i-2]  # 가장 왼쪽이 제일 크다고 가정
        if maxV < H[i-1]:
            maxV = H[i-1]
        if maxV < H[i+1]:
            maxV = H[i+1]
        if maxV < H[i+2]:
            maxV = H[i+2]
        if H[i] > maxV:  # 양쪽 비교 끝나고 제일 큰 값이 H[i]보다 작으면
            result += H[i] - maxV  # 두 항목의 차이가 i에서 조망권 확보되는 세대 수

    print(f'#{tc} {result}')