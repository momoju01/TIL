def palindrome(length, words):
    for word in words:
        for i in range(100 - length + 1):  # 단어 인덱스 길이까지
            for j in range(length // 2):
                k = i + j  # 왼쪽에서부터
                l = i + length - 1 - j  # 오른쪽으로 한 칸 씩
                left = word[k]
                right = word[l]
                if left != right:  # 인덱스 다르면 다음 인덱스
                    break
            else:
                return length  # 길이 리턴
    return 0


for _ in range(1, 11):
    tc = int(input())
    # 가로
    row = [input() for _ in range(100)]
    # 세로
    col = [''.join(pal) for pal in zip(*row)]

    # 가로
    ans = 1
    for length in range(2, 101):
        if length > ans + 2:
            break
        if ans < palindrome(length, row):
            ans = length

    # 세로
    for length in range(ans + 1, 101):
        if length > ans + 2:
            break
        if ans < palindrome(length, col):
            ans = length

    print(f'#{tc} {ans}')