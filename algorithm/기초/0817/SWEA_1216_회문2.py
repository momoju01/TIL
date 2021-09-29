def palindrome(s):
    cnt = 0  # 앞-뒤 일치하는 문자열의 갯수
    for i in range(len(s) // 2):
        if s[i] == s[-i - 1]:  # 앞에서 시작하는 문자열과 뒤에서 시작하는 문자열이 일치하면
            cnt += 1
        else:  # 중간에 다른 글자들이 존재하면
            return False
    if cnt == len(s) // 2:
        return True
    return False


def get_answer(n):
    # 최대 n에서 1씩 감소하는 최대 회문길이 m
    for m in range(n, 1, -1):
        for i in range(n):  # 회문을 시작하는 row idx
            for j in range(n - m + 1):  # i번째 row에서, j부터 m 길이만큼 연속하는 회문 찾기
                # row 기준 arr에서 m길이의 회문을 발견하면
                if palindrome(arr[i][j:j + m]) == True:
                    return m  # 해당 회문 길이 m이 최대이므로 반환
                # col 기준 arr2에서 m길이의 회문을 발견하면
                elif palindrome(arr2[i][j:j + m]) == True:
                    return m
    return 1  # 못 찾으면 길이는 1짜리


N = 100
T = 10
for _ in range(1, T + 1):
    tc = int(input())
    # N, M = map(int, input().split())    # 전체 N * N 크기에서 길이가 M인 회문
    arr = [input() for _ in range(N)]
    # create row <-> col arr2
    arr2 = [[''] * N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            arr2[a][b] = arr[b][a]

    answer = get_answer(N)

    print(f'#{tc} {answer}')