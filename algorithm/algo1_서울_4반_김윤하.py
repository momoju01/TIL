def change(arr):
    # 우측으로 복사하기
    for i in range(len(arr)):
        arr[i] += arr[i][::-1]

    # 아래쪽으로 복사하기
    arr = arr + arr[::-1]
    return arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    org = [list(map(int, input().split())) for _ in range(N)]

    org = change(org)

    # 출력
    print(f'#{tc}')
    for i in range(len(org)):
        for j in range(len(org)):
            print(org[i][j], end=" ")
        print()
