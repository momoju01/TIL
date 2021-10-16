# CAAABBA

T = int(input())
for tc in range(1, T + 1):
    text = list(input())
    stack = []

    for char in text:
        if stack:  # 스택에 뭔가 있으면 비교
            if stack[-1] != char:  # 다르면
                stack.append(char)
            else:                  # 같으면
                stack.pop()
        else:      # 스택에 아무것도 없으면 그냥 append
            stack.append(char)

    print(f'#{tc} {len(stack)}')