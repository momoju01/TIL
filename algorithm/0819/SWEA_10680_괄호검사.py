T = int(input())
for tc in range(1, T+1):
    s = input()
    stack = []
    ans = 1  # 짝이 맞으면 1

    for x in s:
        if x =='(' or x == '{':  # 여는 괄호인 경우
            stack.append(x)     # push(X)

        elif x == ')':  # 닫는 괄호가 소괄호일 때
            if stack != [] and stack[-1] == '(':  # 스택이 비어있지 않고 마지막이 여는 소괄호이면
                stack.pop()
            else:
                ans = 0
                break

        elif x == '}':  # 닫는 괄호가 중괄호일 때
            if stack != [] and stack[-1] == '{':  # 스택이 비어있지 않고 마지막이 여는 중괄호이면
                stack.pop()
            else:
                ans = 0
                break
        # else: # 괄호 아닌 경우(생략)
            # pass

    if stack:  # stack에 여는 괄호 남아있으면
        ans = 0

    print(f'#{tc} {ans}')

