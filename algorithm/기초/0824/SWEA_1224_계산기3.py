for tc in range(1, 11):
    N = int(input())
    s1 = input()
    s2 = ''  # 후위표기식
    stack = []

    # step1
    for x in s1:
        # 피연산자
        if '0' <= x <= '9':
            s2 += x
        # 연산자
        elif x == '(':  # 여는 괄호는 들어올 때 우선순위 가장 높으므로 바로 append
            stack.append(x)
        elif x == '*':
            while stack[-1] == "*":            # 우선순위 낮은 값 나올 때까지 pop하고 후위연산자행
                s2 += stack.pop()
            stack.append(x)
        elif x == '+':
            while stack:
                if stack[-1] == '(':           # 종료조건 :여는 괄호 나올 때까지
                    break
                s2 += stack.pop()              # *랑 + 빼서 후위연산자행
            stack.append(x)
        else:                                  # 닫는 괄호일 때
            while stack:
                if stack[-1] == '(':           # 여는 괄호 나오면 괄호를 제거
                    stack.pop()
                    break
                s2 += stack.pop()              # 여는 괄호 나올 때까지 pop해서 후위표기식 행

    # 스택에 남아있는 것 후위연산자로 빼기
    while stack:
        s2 += stack.pop()
        stack.pop()

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

        else :  # 피연산자
            stack.append(int(x))

    print(f'#{tc} {stack[-1]}')

