# 1차원 배열
# lst = [2, 3, 4]
# lst = [list(map(int, input().split()))]

# lst 5개 받으면 3  * 5 되는데..
# lst =[[0] * 3 ] *5 이렇게 하면 안 되나요? -> 1차원 리스트 만들어 놓은 것을 index  리스트의 전부가 참조함
# shallow copy 됨.

# 그러면 어떻게??

lst = [[0] *3 for _ in range(5)]
# lst[1][1] = 10
# print(lst)

for i in range(5):
    lst[i] = list(map(int, input().split()))


lst = [list(map(int, input().split())) for _ in range(5)] # i를 활용하는 내용이 없어서 _ 로 입력 받음




행 우선

나의 모든 행이 다 끝나야 다음 행으로 갈 수 있음


lst = [[2, 3, 4], [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]

for i in range(5):

ith 행을 먼저
lst[i][0], lst[i][1], lst[i][2]

    for j in range(3):
        print(lst[i][j])



열 우선
i 번째 열은
lst[0][i], lst[1][i], lst[2][i]

for i in range(3):
    print(lst[j][i])
    for j in range(5):
        print(lst[j][i])





# 지그재그
rows =len(lst)
cols = len(lst[0]) # 아무거나  넣어도 됨.. 어차피 모든 열 길이 똑같음


i : 0, 2, 4, 6

m: 20 이라고 가정

for j in range(m):
    print(lst[i][j])



홀수일 때

for j in range(m-1, -1, -1):  #뒤에서부터~~~


프로그램 짜면:

for i in range(rows):
    if i % 2 == 0:
        for j in range(cols):
            print(lst[i][j])
    else:
        for j in range(cols):
            print(lst[i][cols-1-j])

        # for j in range(cols):
        #     print(list[i][j])

# 교재는 i % 2 가 짝수이면 0 이므로 뒤에 사라지고
# i % 2  가 홀수이면 1 이므로 조건 살려져서


