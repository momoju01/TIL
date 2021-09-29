T = int(input())

for tc in range(1, T+1):
    word = [0] *5

    max_len = 0

    for i in range(5):
        word[i] = list(input())  # 문자열로 받아도 됨
        if len(word[i]) > max_len:  # 입력받으면서 최대값도 미리 받아두기
            max_len = len(word[i])

    print(f'#{tc}', end=' ')

    for i in range(15):  # i : 세로로 읽을 열의 인덱스, 가지고 있는 word 중 최고 길이만 돌면 됨
        for j in range(5):  # 무조건 단어 5개 들어오니까 5로 걍 해도됨
            # 1. 허락 받고 쓰자
            # if len(word[j]) > i :    # ★길이  주의
            #     print(word[j][i], end=' ')
            # 2. 허락 말고 용서
            try:
                print(word[j][i], end='')
            except:
                pass
    print()
