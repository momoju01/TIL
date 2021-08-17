# 첫 번째 방법

for _ in range(1, 11):
    tc = int(input())
    N = 100
    arr = [list(input()) for _ in range(N)]
    res = 1

    for M in range(100, 0, -1):  # 회문의 길이 후보
        if res != 1:
            break
        # 행
        for i in range(N):
            if res != 1:
                break
            for j in range(N - M + 1):
                temp = 0
                for k in range(M // 2):
                    if arr[i][j+k] == arr[i][j+M-k-1]:
                        temp += 1
                if temp == M //2:   # 같은 단어의 수가 단어의 절반 길이와 같은지 확인
                    res = M
                    break
                # 열
                temp = 0
                for k in range(M // 2):
                    if arr[j + k][i] == arr[j + M - k - 1][i]:
                        temp += 1
                if temp == M // 2:
                    res = M

    print(f'#{tc} {res}')



# 요약하지 않은 버젼

for _ in range(1, 11):
    tc = int(input())
    N = 100
    arr = [list(input()) for _ in range(N)]
    res = 1

    for M in range(100, 0, -1):  # 회문의 길이 후보
        if res != 1:
            break
        # 행
        for i in range(N):
            if res != 1:
                break
            for j in range(N - M + 1):
                temp = 0
                for k in range(M // 2):
                    if arr[i][j+k] == arr[i][j+M-k-1]:
                        temp += 1
                if temp == M //2:   # 같은 단어의 수가 단어의 절반 길이와 같은지 확인
                    res = M

        # 열
        for i in range(N):  # i 가 열
            for j in range(N - M + 1):
                temp = 0
                for k in range(M // 2):
                    if arr[j + k][i] == arr[j + M - k - 1][i]:
                        temp += 1
                if temp == M // 2:
                    res = M

    print(f'#{tc} {res}')


# 두 번째 풀이
# 회문인지 확인하는 함수
def palindrome(word, m):
    for i in range(m // 2):
        if word[i] != word[-1 - i]:
            return False
    return True


for _ in range(1, 11):
    tc = int(input())
    n = 100
    words = []
    for _ in range(n): # 가로를 분석하기 위한 words
        words.append(input())
    # 통으로 받으려면 이렇게 하면 됨 : arr = [input() for _ in range(N)]

    words_h = [''.join(i) for i in zip(*words)]  # 세로를 쉽게 분석하기 위한 words_h

    res = 1
    flag = False

    # 효율을 위해 큰 값에서 작은값으로 진행
    for m in range(100, 1, -1):
        for i in range(n):
            for j in range(n - m + 1):
                # 가로 또는 세로에 회문이 있다면, 저장 후 for문 종료
                if palindrome(words[i][j:j + m], m) or palindrome(words_h[i][j:j + m], m):
                    res, flag = m, True
                    break
            if flag:
                break
        if flag:
            break

    print(f'#{tc} {res}')

