for tc in range(1, 11):
    N = int(input())
    s1 = input()
    s2 = ''  # 후위표기식
    stack = []

    # step1
    for x in s1:
        # 피연산자는 바로 출력
        if '0' <= x <= '9':
            s2 += x
        # 연산자는 stack 에 push
        elif x == '*':  # 곱셈인 경우
            while stack and stack[-1] == "*":  # 스택이 있고, top의 값이 *라면
                s2 += stack.pop()  # 다 빼서 후위표기식에 넣고
            stack.append(x)  # 방금 들어온 곱셈 넣어주기
        else:  # 덧셈인 경우 다 빼고 넣기
            while stack:
                s2 += stack.pop()
            stack.append(x)
    # 스택에 남아있는 것 다 빼서 후위연산자에 넣기
    while stack:
        s2 += stack.pop()


    # step2 : 후위표기식 사용하여 연산

    for x in s2:
        if x == '+':
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2 + op1)

        elif x == '*':
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2 * op1)

        else :          # 피연산자
            stack.append(int(x))

    print(f'#{tc} {stack[-1]}')

