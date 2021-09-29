def push(item):
    return ST.append(item)
    # if isFull():
    #     return False
    # top 1 증가
    # 데이타(item)를 스택에 추가한다
    #
    # return True

def pop():
    if len(ST) > 0 :  # 스택 비어있지는 않은지 확인
        return ST.pop(-1)
    return -1  # -1 나오면 데이터 없는 걸로 생각하기
#     top에 있는 데이타를 return
#     top을 하나 뺀다.
#     result
#     return top에 있는 데이타




def peek():
    return ST[-1]
    # top에 있는 데이타를 return


ST = []
push(1)
push(2)
value = pop()
value = pop()
value = pop()
# value = peek()