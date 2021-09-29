T = int(input())

for T in range(1, T + 1):
    word = input()
    text = input()
    N = len(text)
    M = len(word)
    count_str = [0] * M

    # word와 일치하는 숫자 세기
    for i in range(M):
        for j in range(N):
            if word[i] == text[j]:
                count_str[i] += 1

    # 최대값 구하기
    count_max = 0
    for i in count_str:
        if i > count_max:
            count_max = i

    print(f'#{T} {count_max}')