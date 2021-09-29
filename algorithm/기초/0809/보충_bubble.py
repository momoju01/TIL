lst = [55, 7, 78, 12, 42]
N = len(lst)

# 첫 번째 패스에서 할 일: N-1(4)번째로 큰 값을 구해서 lst[N-1]
#     0-1, 1-2, 2-3, 3-4 비교
# 두 번째 패스에서 할 일: N-2(3)번째로 큰 값을 구해서 lst[N-2]
#     0-1, 1-2, 2-3
# i 번째 패스에서 할 일: i번째로 큰 값을 구해서 lst[i]
#     0-1, 1-2 ---> lst[i-1]-lst[i]


for i in range(N-1, 0, -1):
    for j in range(0, i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)