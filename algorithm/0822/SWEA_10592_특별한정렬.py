T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 리스트 길이
    lst = list(map(int, input().split()))
    n_lst = [0] * 10

    # 선택정렬 : 제일 작은 것 찾으면
    for i in range(0, N - 1):  # 0 -> n-2까지만 실행하면 됨
        minIdx = i
        for j in range(i + 1, N):
            if lst[j] < lst[minIdx]:
                minIdx = j
        lst[i], lst[minIdx] = lst[minIdx], lst[i]
    print(lst)
    # # 새로운 리스트에 차례로 정렬하기
    # for n in range(-1, -6, -1):  # 최대값 5개 큰 순으로
    #     n_lst[(-2) * n - 2] = lst[n]  # 새로운 리스트의 짝수 인덱스에 넣기
    # for n in range(5):
    #     n_lst[2 * n + 1] = lst[n]  # 홀수 인덱스에 최소값
    #
    # print(f'#{tc}', end=' ')
    # for n in n_lst:
    #     print(n, end=' ')
    # print()