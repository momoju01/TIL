top = -1
stack = [0]* 10

top += 1
stack[top] = 1

top += 1
stack[top] = 2

top += 1
stack[top] = 3


while top > -1:
    print(stack[top])
    top -= 1


front = -1
rear = -1
q = [0]* 100

rear += 1
q[rear] = 2

rear += 1
q[rear] = 2

rear += 1
q[rear] = 3


while front != rear:
    front += 1
    print(q[front])