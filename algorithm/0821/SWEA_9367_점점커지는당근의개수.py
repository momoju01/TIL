T = int(input())
for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    max_len = 1
    temp_len = 1

    for i in range(N):
        if i != N-1 and lst[i+1] - lst[i] == 1 :
            temp_len += 1
        else:
            if temp_len > max_len:
                max_len = temp_len
            temp_len = 1  # temp_len 초기화


    print(f'#{tc+1} {max_len}')

