# 조상 찾기
"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

6
1 2 1 3 2 4 3 5 3 6
"""

V = int(input())
edge = list(map(int, input().split()))
E = V - 1
left = [0] * (V+1)  # 모부 번호를 인덱스로 자식 번호 저장
right = [0] * (V+1)
par = [0] * (V+1)   # 자식 인덱스로 모부번호 저장

for i in range(E):
    p, c = edge[2*i], edge[2*i+1]
    if left[p] == 0:    # p의 왼쪽 자식이 없으면
        left[p] = c
    else:               # 왼쪽 자식 있으면 오른쪽 자식으로 저장
        right[p] = c
    par[c] = p          # 0(0), 0, 1, 1, 2, 3, 3
                        # (1) 조상을 찾는 데 사용
                        # (2) root 찾기

#
# # c의 조상 찾기
# c = 6
# while par[c]:       # 모부가 있으면
#     print(par[c])
#     c = par[c]
#                     # 모부가 없으면 while문 빠져나옴


# 모부가 없으면 root
root = 1
while par[root]:    # root 로 추정한 정점이 모부가 있으면
    root += 1

print(root)