def merge(left,right):
    # arr1과 arr2를 병합한 배열을 반환
    global cnt
    result = []

    if left[-1] > right[-1]:
        cnt += 1
    #병합하기
    i = j = 0
    # 복사할 배열 요소가 남아있으면 계속 반복
    left_len = len(left)
    right_len = len(right)
    while i < left_len or j < right_len:
        # 1. left와 right에 모두 복사할 요소가 남아있는경우
        # 2. left에만 남아있는 경우
        # 3. right에만 남아있는경우
        if i < left_len and j < right_len:  # 1번
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i < left_len:  # 왼쪽 요소만 남음..
            result.append(left[i])
            i += 1
        elif j < right_len:  # 오른쪽 요소만 남음
            result.append(right[j])
            j += 1

    return result

def merge_sort(arr):
    # 만약 두 부분으로 나눌 수 없다면, 과정없이 arr을 그대로 반환
    if len(arr) == 1:
        return arr
    # 전체를 두 부분으로 나누는 부분
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    # 나뉜 두 부분을 각각 merge_sort()를 실행
    left = merge_sort(left)
    right = merge_sort(right)
    # 각각에 대한 merge_sort()의 결과를 병합
    # 병합(merge) : 두 배열에서 작은 순서대로 요소를 가져와서 새로운 배열 만들기
    # 병합한 배열 반환
    return merge(left,right)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    
    result = merge_sort(arr)[N//2]
    print(f'#{tc} {result} {cnt}')
