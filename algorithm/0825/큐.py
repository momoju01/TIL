Q =[0] * 10  # 10칸짜리 큐
front = -1
rear = -1

rear += 1
Q[rear] = 1    # enQueue(1)

rear += 1
Q[rear] = 2    # enQueue(2)

rear += 1
Q[rear] = 3    # enQueue(3)

while front != rear:
    front += 1
    print(Q[front], end =' ')  # print(deQueue())
print()


# list로 구현
listQ = []
listQ.append(1)
listQ.append(2)
listQ.append(3)
while listQ:
    print(listQ.pop(0), end=' ')
print()


# 참고
from collections import deque

# enqueue -> append
q = deque()
q.append(1)
q.append(2)
q.append(3)

# deque -> popleft

while q:
    print(q.popleft())