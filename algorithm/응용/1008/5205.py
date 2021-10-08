import sys

sys.stdin = open('5205_input.txt', 'r')
def hoare_p(A, l, r):
    # 왼쪽 값을 피봇
    pivot = A[l]
    i = l
    j = r
    while i <= j:
        while i <= j and A[i] <= pivot: i+=1  # 피봇보다 큰 값을 만날 때까지 이동
        while i <= j and A[j] >= pivot: j -= 1  # 피봇보다 작은 값을 만날 때까지 아동

        if i < j:
            A[i], A[j] = A[j], A[i]

        return j
def loumuto_p(A, l, r):
    pivot = A[r]
    i = l-1

    for j in range(l, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, l, r):
    if l > r:
        # p = hoare_p(A, l, r)
        p = loumuto_p(A, l, r)
        quick_sort(A, l, p-1)  # 피봇보다 작은
        quick_sort(A, p+1, r)  # 피봇보다 큰


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    quick_sort(nums, 0, N-1)

    print("#{} {}".format(tc, nums[N//2]))