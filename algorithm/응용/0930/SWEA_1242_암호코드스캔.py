import sys
sys.stdin = open("input.txt", "r")

number = {'112': 0, '122': 1, '221': 2, '114': 3, '231': 4, '132': 5, '411': 6, '213': 7, '312': 8, '211': 9}
binary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
          '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # hexa = "123456789ABCDEF"  # 0은 일단 제외
    # code = ''  # 16진수로 된 코드 넘버 저장
    #
    # for i in range(N):
    #     tmp = input()
    #     for j in range(M):  # 가로
    #         if M[j] in tmp:    # 문자열이 있는 행이라면
    #             tmp.strip('0')
    #             print(tmp)
    #             break
    #         else:
    #             continue

    big_code = [input()[:M] for _ in range(N)]
    visited = []
    ans = 0
    for n in range(N):
        binarified = ''
        for char in big_code[n]:
            binarified += binary[char]
        big_code[n] = binarified
    res = []
    print(binarified)

