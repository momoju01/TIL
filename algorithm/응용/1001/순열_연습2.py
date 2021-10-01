def f(i, N):
    global ans
    if i == N:  # 순열 완성
        print(arr)
        # 베이비진 판정
        run = 0
        tri = 0
        if arr[0]+1 == arr[1] and arr[1]+1 == arr[2]:  #왼쪽 절반이 run인 경우
            run += 1
        if arr[0] == arr[1] == arr[2]:
            tri += 1
        if arr[3]+1 == arr[4] and arr[4]+1 == arr[5]:   # 오른쪽 절반이 run인 경우
            run += 1
        if arr[3] == arr[4] == arr[5]:
            tri += 1
        if run + tri == 2:
            ans = 1

    else:
        for j in range(1, N):  #arr[i]와 교환할 위치
            arr[i], arr[j] = arr[j], arr[i]
            f(i+1, N)
            arr[i], arr[j] = arr[j], arr[i]

arr = list(map(int, input()))
ans = 0
f(0, 6)
print(ans)