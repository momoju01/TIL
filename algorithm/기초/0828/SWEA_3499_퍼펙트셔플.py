T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(input().split())
    l = 0           # 왼쪽 더미 인덱스
    r = (N+1)//2    # 오른쪽 더미 인덱스
    new = []

    for _ in range(N//2):
        new.append(lst[l])  # 왼쪽 더미
        new.append(lst[r])  # 오른쪽 더미
        l, r = l+1, r+1

    if N % 2:       # 더미가 홀수라면 맨 마지막 남은 장수 더해줘야됨
        new.append(lst[N//2])



    print('#{0}'.format(tc), ' '.join(new))  #join(map(str, new))도 됨