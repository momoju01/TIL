import sys
sys.stdin = open('input_4366.txt', 'r')


# num : 문자열 (미리 수정해놓고 와도 좋다)
def change_to_dec(num, notation):
    tmp = 0



    for n, val in enumerate(list(map(int, num))[::-1]):
        tmp += val*(notation ** n)
    return tmp


# # enmuerate 몰라!
# def change_to_dec2(num, notation):
#     tmp = 0
#     n = len(num)-1
#     for i in map(int, num):
#         tmp += i * (notation**n)
#         n -= 1
#
#     return tmp
#
# def check(num, notation):
#     change_num = change_to_dec(num, notation)
#     # change_num = int(num, notation)
#
#     for n, val in enumerate(list(map(int, num))[::-1]):
#         for j in range(notation):
#             if val == j : continue
#             tmp = change_num - val * (notation ** n) + j * (notation ** n)
#             if tmp not in binary:
#                 binary.append(tmp)
#             else:
#                 return tmp



def check2():
    bi_num = 0
    for x in bi:
        bi_num = bi_num * 2 + int(x)  # 자릿수 밀어버리기

    for i in range(len(bi)):  # bi길이만큼 돌면서
        binary.append(bi_num ^ (1<<i))  # i 자리만 토글된 값 얻을 수 있음

    for i in range(len(tr)): # ex(212)  # i는 바꿀 자리
        num1 = 0  #112
        num2 = 0  #012
        for j in range(len(tr)):  # j : 바꿀 값
            if i != j:  # i가 현재 바꾸고 싶은 자리 가르키고 있어서 서로 다르면 바꾸면 안됨
                num1 = num1 * 3 + int(tr[j])
                num2 = num2 * 3 + int(tr[j])
            else:
                num1 = num1 * 3 + (int(tr[j]) + 1) % 3  # 0->1 1->2 2->0
                num2 = num2 * 3 + (int(tr[j]) + 2) % 3  # 0->2 1->0 2->1

        if num1 in binary:
            return num1
        if num2 in binary:
            return num2


T = int(input())

for tc in range(1, T+1):
    bi = input()
    tr = input()
    #
    binary = []
    # check(bi, 2)

    # print(binary)  # [11, 8, 14, 2]

    # print(f'#{tc} {check(tr, 3)}')
    print(f'#{tc} {check2()}')