T = int(input())

def div(num):
    return (int(num) + 1) // 2


for tc in range(1, T+1):
    N = int(input())  # 돌아가야 할 사람의 수

    students =[list(map(div, input().split())) for _ in range(N)]
    # print(student)

    corridor =[0] * 201  # 복도 개수 0~200

    for i in range(N):
        if students[i][0] > students[i][1]:
            students[i][0], students[i][1] = students[i][1], students[i][0]
        for j in range(students[i][0], students[i][1]+1):
            corridor[j] += 1

    print(f'#{} {max(corridor)}')