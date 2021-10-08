import sys
sys.stdin = open('input_4366.txt', 'r')

def f():
    # bint = int(b, 2)
    bint = 0
    for x in b:
        bint = bint*2 + int(x)
    binary = []
    for i in range(len(b)):
        binary.append(bint ^ (1<<1))  # 2진수의 1비트씩을 바꿔서 저장

    for i in range(len(t)):  # 3진수에서 다른 두 수로 바꿔볼 자리
        num1 = 0
        num2 = 0
        for j in range(len(t)):
            if i != j:
                num1 = num1*3 + int(t[j])
                num2 = num2*3 + int(t[j])
            else:
                num1 = num1*3 + (int(t[j]) + 1) % 3  # 0->1 1->2 2->0
                num2 = num2*3 + (int(t[j]) + 2) % 3  # 0->2 1->0 2->1

        if num1 in binary:
            return num1
        if num2 in binary:
            return num2


T = int(input())
for tc in range(1, T+1):
    b = input()
    t = input()
    #
    binary = []


    print(f'{tc} {f()}')