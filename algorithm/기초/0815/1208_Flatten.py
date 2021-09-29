for tc in range(10):
    dump = int(input())
    arr = list(map(int, input().split()))
    diff = 0

    while dump:  # 덤프 횟수 남아 있을 때까지
        maxI = 0
        minI = 0
        # 최대값과 최소값의 인덱스 찾기
        for i in range(len(arr)):
            if arr[i] > arr[maxI]:
                maxI = i
            if arr[i] < arr[minI]:
                minI = i

        # dump
        arr[maxI] -= 1
        arr[minI] += 1
        dump -= 1

    #최대값 최소값 다시 찾기..
    for i in range(len(arr)):
        if arr[i] > arr[maxI]:
            maxI = i
        if arr[i] < arr[minI]:
            minI = i
    diff = arr[maxI] - arr[minI]


    print(f'#{tc+1} {diff}')



