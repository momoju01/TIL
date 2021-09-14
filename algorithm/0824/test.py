for t in range(1, 11):
    n = int(input())
    a = input()

    stack = []
    s2 = ''
    for i in a:
        if '0' <= i <= '9':
            s2 += i
        elif i == "(":
            stack.append(i)
        elif i == "+":
            while stack:
                if stack[-1] == '(':
                    break
                s2 += stack.pop()
            stack.append(i)
        elif i == "*":
            while stack[-1] == "*":
                s2 += stack.pop()
            stack.append(i)
        elif i == ")":
            while stack:
                if stack[-1] == "(":
                    stack.pop()
                    break
                s2 += stack.pop()

    stack = []
    for x in s2:
        if x == "+":
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2 + op1)
        elif x == "*":
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2 * op1)
        else:
            stack.append(int(x))
    print(f'#{t} {stack[0]}')