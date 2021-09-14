T = int(input())
for tc in range(1, T+1):
    s1 = list(input().split())
    stack =[]

    for x in s1:
        # 종료 조건
        if x == ".":
            if len(stack) == 1:
                print(f'#{tc} {int(stack[0])}')
                break
            else:
                print(f'#{tc} error')
                break
        
        # 계산
        elif x.isdigit():
                stack.append(int(x))
        else:
            if len(stack) >= 2:  # 스택에 원소 2개 이상일
                op1 = stack.pop()
                op2 = stack.pop()
                if x == "+":
                    stack.append(op2+op1)
                elif x == "-":
                    stack.append(op2-op1)
                elif x == '*':
                    stack.append(op2*op1)
                elif x == '/':
                    stack.append(op2/op1)

            else:  # 스택에 2 개 이상 없으면
                print(f'#{tc} error')
                break






