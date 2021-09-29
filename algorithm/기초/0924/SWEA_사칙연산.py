# # 교수님 풀이
#
# def calc(v):
#     if len(tree[v]) == 2:
#         return tree[v][1]
#     else:
#         L = calc(tree[v][2])
#         R = calc(tree[v][3])
#
#         if tree[v][1] == '+': return L+R
#         elif tree[v][1] == '-': return L-R
#         elif tree[v][1] == '*': return L*R
#         elif tree[v][1] == '/': return L/R
#
#
# for tc in range(1, 11):
#     N = int(input())  # 정점의 총 수
#     tree = [0] * (N+1)
#
#     for i in range(1, N+1):
#         tmp = input().split()
#         tree[int(tmp[0])] = tmp
#
#         # tmp 길이가 4일때, 0번 인덱스: 정점 번호, 1번 인덱스: 연산자, 2번 인덱스:왼쪽자식번호, 3번 인덱스:오른쪽자식번호
#         if len(tmp) == 4:
#             tree[int(tmp[0])][2] = int(tree[int(tmp[0])][2])
#             tree[int(tmp[0])][3] = int(tree[int(tmp[0])][3])
#         else:
#             tree[int(tmp[0])][1] = int(tree[int(tmp[0])][1])
#
#     print("#{} {}".format(tc, int(calc(1))))
#

# 교수님 풀이
def calc(v):
    if len(tree[v]) == 2:
        return int(tree[v][1])
    else:
        L = calc(int(tree[v][2]))
        R = calc(int(tree[v][3]))

        if tree[v][1] == '+':
            return L+R
        elif tree[v][1] == '-':
            return L-R
        elif tree[v][1] == '*':
            return L*R
        elif tree[v][1] == '/':
            return L/R


for tc in range(1, 11):
    N = int(input())  # 정점의 총 수
    tree = [0] * (N+1)

    for i in range(1, N+1):
        tmp = input().split()
        tree[int(tmp[0])] = tmp

    print("#{} {}".format(tc, int(calc(1))))