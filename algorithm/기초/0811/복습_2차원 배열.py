# # 2차원 배열의 생성
#
# N, M = map(int, input().split())
#
# arr = [[0] * M for _ in range(N)]
#
#
# # 배열 순회
# # 행 우선 순회
#
# for i in range(N):  # == len(arr) # N 없어도 list 주어지면 len으로 구하면 됨
#     for j in range(M):  # ==len(arr[0]) # arr[0]이든 [1]이든 상관 X
#         arr[i][j]
#
# # 열 우선 순회
# # i 가 열인 경우
#
# for i in range(M):
#     for j in range(N):
#         arr[j][i]
#
#
# # 지그재그 순회
# # N = 2
# # M = 3
# # arr = [[1, 2, 3], [3, 4, 5]]
# for i in range(N):
#     if i % 2 == 0:
#         for j in range(M):
#             print(arr[i][j])
#     else:
#         for j in range(M-1, -1, -1):
#             print(arr[i][j])
#
#
#

# 델타를 이용한 2차원 배열 탐색
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 첫 번째 방법

###### 우 하 좌 상
drow =[0, -1, 0, 1]
dcol =[1, 0, -1, 0]

for row in range(len(arr)):
    for col in range(len(arr[0])):
        for f in range(4):  #방향 4개
            nrow = arr[row] + drow[f]
            ncol = arr[col] + dcol[f]
            if 0 <= nrow < N and 0 <= ncol < M:  #사용 범위 확인. 추가해야하면 더 추가하기
                arr[nrow][ncol]

# 두 번째 방법

for r in(N):
    for c in(M):
        for dr, dc in [[0, 1], [-1, 0], [0, -1], [1, 0]]
            nr = arr[r] + dr
            nc = arr[c] + dc
            if 0 <= nr < N and 0 <= nc < M :
                arr[nr][nc]

