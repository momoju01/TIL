T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    maxV = -1  # 단조 증가 아닌 경우 -1 출력

    for i in range(N-1):          # 곱셈
        for j in range(i+1, N):
            num = lst[i] * lst[j]
            temp = str(num)       # string으로 형변환
            flag = True
            l = len(temp)         # string 길이

            # if num < maxV:      # 단조 증가하는 값 저장해둔 maxV 보다 작으면 단조증가하는지 검사 안해도 됨
            #     break           # 이거땜에 오류 계속 남... !! !! 일케 하면 왜 안 되는지 알려조...

            # 단조증가 검사
            for k in range(l-1):
                if temp[k] > temp[k+1]:  # 단조 증가 안하면 중단
                    flag = False
                    break
            if flag:              # 단조 증가하면(위 for문에서 flag False로 안 바뀐)
                if num > maxV:
                    maxV = num

    print('#{} {}'.format(tc, maxV))

