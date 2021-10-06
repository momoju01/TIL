def merge_sort(num):
    if len(num) == 1:  # 길이가 1이면
        return num  # 길이가 1인 리스트 num이 그대로 리턴

    middle = len(num) // 2  # 중앙값
    left = merge_sort(num[:middle])  # 왼쪽 리스트
    right = merge_sort(num[middle:])  # 오른쪽 리스트

    return merge(left, right)


def merge(left, right):
    global ans
    result = []
    left_idx = 0
    right_idx = 0

    if left[-1] > right[-1]:
        ans += 1

    while left_idx < len(left) or right_idx < len(right):  # left나 right 리스트가 둘 중 하나라도 있으면
        if left_idx < len(left) and right_idx < len(right):  # 둘다 있는 경우,
            if left[left_idx] <= right[right_idx]:  # 값이 작은 쪽을 결과 리스트에 넣기
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
        elif left_idx < len(left):  # 왼쪽만 있는 경우
            result.append(left[left_idx])
            left_idx += 1
        else:  # 오른쪽만 있는 경우
            result.append(right[right_idx])
            right_idx += 1
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    ans = 0
    num = merge_sort(num)

    print(f'#{tc} {num[N // 2]} {ans}')