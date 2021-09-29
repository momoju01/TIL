T = int(input())

for tc in range(1, T+1):
    N = int(input())  # N: 날짜 수
    chart = list(map(int, input().split()))  # 각 날의 매매가
    maxV = chart[-1]  # 가장 최근 날짜의 가격을 최대값으로 설정
    rev = 0

    # 뒤에서 세는 방식
    for i in range(N-2, -1, -1):
        if chart[i] < maxV :  #직전 날 가격이 최대값보다 작으면 수익발생
            rev += maxV - chart[i]
        else:  # 가격이 같거나 크면 새로운 최대값으로 설정
            maxV = chart[i]

    print(f'#{tc} {rev}')
