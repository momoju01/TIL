# 정수를 저장하는 스택을 구현


class Stack():
    def __init__(self):
        self.stack = []
    
    # push X: 정수 X를 스택에 넣는 연산이다. 
    def push(self, i):
        self.stack.append(i) #append로 리스트 맨 마지막에 추가

    # pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
    # 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

    def pop(self):
        if self.stack == []:
            return -1
        else:
            return self.stack.pop()
    
    # size: 스택에 들어있는 정수의 개수를 출력한다. 
    # 정수를 저장하는 스택이니 int인지 확인 필요x
    def size(self):
        return len(self.stack)

    # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    def empty(self):
        if self.stack: #머라도 있으면0
            return 0
        else:  # 비어있으면
            return 1

    # top: 스택의 가장 위에 있는 정수를 출력한다. 
    # 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def top(self):
        if self.stack == []:
            return -1
        else:
            return self.stack[-1]

# 입력... 무리... 
