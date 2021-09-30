import sys

sys.stdin = open("input.txt", "r")

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    # 암호패턴 정보
    secret_key = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6,
                  '0111011': 7, '0110111': 8, '0001011': 9}

    # 주어진 암호 정보 담을 리스트
    secret = []

    for _ in range(N):
        num = input()
        # 암호안에 1이 들어있고 암호정보가 비어있을 경우
        if '1' in num and not secret:
            # rindex를 이용하여 1의 맨 뒤 인덱스를 가져옵니다.
            # 길이를 총 56으로 한 뒤 7씩 끊어가면서 암호패턴 정보의 key값을 가지는 번호를 가져옵니다.
            secret = [secret_key[num[i - 6:i + 1]] for i in range(num.rindex('1'), num.rindex('1') - 56, -7)]

            # 짝수 자리는 3배, 홀수 자리는 1배수로 해서 저장한 리스트의 합을 저장
            odd = sum([secret[i] * 3 if i % 2 else secret[i] for i in range(len(secret))])
    # 더한 값을 10으로 나웠을 때 0이 아니면 0을 출력, 0이면 원래 암호 정보의 합을 출력
    if odd % 10:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {sum(secret)}')