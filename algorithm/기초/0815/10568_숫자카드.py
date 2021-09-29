T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    count = [0] * 10  # 카드에 0 없지만 일단 만들어주고

    for i in arr:  # arr에 있는 숫자를 인덱스로 하는 count 리스트에 더해주기
        count[i] += 1  # arr[0] 이 4면 count[4]에 1 추가

    # count 에서  max 값과 몇 장 있는지 찾기
    maxIdx = 0
    for i in range(1, 10):  # 0 없으니 1부터 찾기
        if count[i] > count[maxIdx]:
            maxIdx = i

    print(f'#{tc} {maxIdx} {count[maxIdx]}')
