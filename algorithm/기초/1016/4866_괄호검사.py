# 정상 : 1 아니면 : 0 출력

T = int(input())
for tc in range(1, T + 1):
    text = list(input())

    stack = []
    ans = 1

    for i in text:
        if i =='(' or i == '{':  # 여는 괄호이면
            stack.append(i)      # push

        elif i == ')':
            if stack != [] and stack[-1] == '(':
                stack.pop()
            else:
                ans = 0
                break
        elif i == '}':
            if stack != [] and stack[-1] == '{':
                stack.pop()
            else:
                ans =0
                break
        else:
            pass

    if stack:
        ans = 0


    print(f'#{tc} {ans}')