s = input()
stack =['']*100
top = -1
ans = 1

for x in s :  # 한 글자씩...
    if x == '(':  # push(x)
        top += 1
        stack[top] = x
    elif x == ')':  # pop()한 결과와 비교. 스택이 비어있으면 오류(중단)
        if top >= 0: # 스택이 비어있지 않으면
            top -= 1
            stack[top +1]  # 소괄호만 있으므로 비교 생략
        else:  # 여는 괄호가 부족하면(닫는 괄호가 나왔으나 여는 괄호 부족)
            ans = 0
            break
    else:
        pass # 괄호가 아닌 경우...

# 스택에 남은 괄호과 있는지 확인

if ans and top >= 0:  #  닫는 괄호가 더 이상 없으나 여는 괄호가 남은 경우
    ans = 0
print(ans)
