
import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    # 암호 코드
    secret_code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6,
                  '0111011': 7, '0110111': 8, '0001011': 9}


    code = []           # 10진수로 된 코드 넘버
    sum_code = 0        # 합 저장
    for _ in range(N):
        num = input()
        # 1. 8자리 숫자 찾기
        if '1' in num and not code:  # 1이 있는 행을 발견하면 맨 마지막에 있는 1의 인덱스를 가져옴
            idx = num.rindex('1')
            for i in range(idx, idx - 56, -7):
                code.append(secret_code[num[i - 6:i + 1]])  # 역순으로 저장됨

            # 2. 암호 코드 계산하기
            for i in range(len(code)):
                if i %2:  # 검증 코드가 0번 인덱스
                    sum_code += code[i] * 3
                else:
                    sum_code += code[i]

    # 3. 검증 코드 맞는지 확인 후 출력
    if sum_code % 10:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {sum(code)}')