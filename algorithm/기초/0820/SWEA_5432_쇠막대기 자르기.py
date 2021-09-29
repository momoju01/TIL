T = int(input())
for tc in range(1, T+1):
    bar = input()  # 스트링으로 받기
    stack = []
    res = 0

    for i in range(len(bar)):
        if bar[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if bar[i - 1] == '(':  # 레이저이면
                res += len(stack)
            else:  # 괄호 끝났으면
                res += 1  # 마지막 조각 넣어주고


    print(f'#{tc} {res}')
