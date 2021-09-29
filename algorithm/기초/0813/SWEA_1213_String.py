# 고지식한 패턴 알고리즘


for T in range(1, 11):
    tc = int(input())
    word = list(input())
    text = list(input())
    count = 0

    for i in range(len(text)-len(word)+1):  # i 는 word의 길이만큼은 실행 안 해도 됨
        for j in range(len(word)):
            # 불일치
            if word[j] != text[i+j]:  # text 인덱스에 j 더하는 거 잊지 말기...
                break  # i+1
        # 인덱스 j의 원소 다 일치해야 else 실행됨
        else:
            count += 1

    print(f'#{tc} {count}')

for _ in range(10):
    case = int(input())
    word = input()
    sentence = input()
    res = 0
    for i in range(len(sentence) - len(word) + 1):
        for j in range(len(word)):
            if sentence[i + j] != word[j]:
                break
        else:
            res += 1

    print(f'#{case} {res}')