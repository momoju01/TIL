s1 = '2+3*4/5'

# step1
stack = []
s2 = ''

for x in s1:
    # 피연산자는 바로 출력
    if '0' <= x <= '9':
        s2 += x
    # 연산자는 stack 에 push
    else:
        stack.append(x)
while stack:
    s2 += stack.pop()

print(s2)

# step2

for x in s2:
    if x == '+':
        op1 = stack.pop()
        op2 = stack.pop()
        stack.append(op2 + op1)

    elif x == '*':
        op1 = stack.pop()
        op2 = stack.pop()
        stack.append(op2 * op1)

    elif x == '-':
        op1 = stack.pop()
        op2 = stack.pop()
        stack.append(op2 - op1)

    elif x == '/':
        op1 = stack.pop()
        op2 = stack.pop()
        stack.append(op2 / op1)  # //인 경우 2 3 4 * 5 / +

    else :          # 피연산자
        stack.append(int(x))
print(stack.pop())
