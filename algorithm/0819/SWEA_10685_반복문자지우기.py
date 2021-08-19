T = int(input())

for tc in range(1, T+1):
    s = input()
    stack = []
    for char in s:
        if stack:  # 스택에 무언가 있는 경우 꺼내서 비교
            t = stack.pop()
            if t != char:  # 다르면 스택에 순서대로 쌓음
                stack.append(t)
                stack.append(char)
        else:
            stack.append(char)  # 스택에 아무것도 없는 경우 push

    print(f'#{tc} {len(stack)}')