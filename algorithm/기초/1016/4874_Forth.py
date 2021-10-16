"""
연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
‘.’은 스택에서 숫자를 꺼내 출력한다.
나눗셈의 경우 항상 나누어 떨어진다.
error : 연산자가 많거나 숫자가 많거나
"""

T = int(input())
for tc in range(1, T + 1):
    stack = []
    lst = list(map(str, input().split()))  # 문자열로 받기


    for i in lst:
        # 종료조건
        if i == '.':
            if len(stack) == 1:                 # '.'은 push 안 했으니 스택에 맨 마지막까지 남은 숫자가 계산한 결과 값
                print(f'#{tc} {int(stack[0])}')
                break
            else:
                print(f'#{tc} error')  # error1: 숫자가 연산자 수보다 많은 경우
                break

        # 계산
        # 연산자인 경우
        elif i in ['+', '-', '*', '/']:
            if len(stack) >= 2:  # 스택에 원소 2개 이상일 경우
                num2 = stack.pop()  # 먼저 뽑는게 뒤에 가야됨
                num1 = stack.pop()
                if i == '+':
                    stack.append(num1 + num2)
                elif i == '-':
                    stack.append(num1 - num2)
                elif i == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(num1 / num2)
            # error2: 연산자가 숫자보다 많은 경우
            else:  # 스택에 2 개 이상 없으면
                print(f'#{tc} error')
                break

        # 숫자인 경우
        else:
            stack.append(int(float(i)))  # 문자열은 int로 바로 형변환 못 해서 float -> int로

