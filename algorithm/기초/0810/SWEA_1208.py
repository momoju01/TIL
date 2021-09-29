T = 10

for tc in range(1, T+1):
    dump = int(input())  # dump 횟수
    box_list = list(map(int, input().split()))  # 박스 높이


    while dump:  # dump 횟수가 0이 될 때까지 반복
            box_list[box_list.index(max(box_list))] -= 1  #최대값의 인덱스를 찾아서 그 값에서 -1
            box_list[box_list.index(min(box_list))] += 1  #최소값의 인덱스를 찾아서 그 값에서 +1
            dump -=1  # dump 횟수 감소

    print(f'#{tc} {max(box_list)-min(box_list)}')