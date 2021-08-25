def enq(data):
    global qsize
    global rear
    global front
    if (rear+1) % qsize == front:
        # print('Full')
        front = (front+1) % qsize  # 덮어 쓸 때는 비워졌다고 치기(front 하나 올리기)

    rear = (rear+1) % qsize
    q[rear] = data

front = 0
rear = 0
qsize = 4
q= [0] * qsize
enq(1)
enq(2)
enq(3)
enq(4)  # 한 칸은 비워두기로 했으니, qsize보다 한 칸 작은 것 까지만 입력받을 수 있다.
enq(5)

while front != rear:
    front = (front + 1) % qsize
    print(q[front])