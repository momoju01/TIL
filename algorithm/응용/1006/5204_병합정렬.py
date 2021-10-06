def merge(arr1, arr2):
    # arr1과 arr2를 병합한 배열을 반환
    global cnt
    result = []

    if arr1[-1] > arr2[-1]:
        cnt += 1
    # 병합하기
    while len(arr1) > 0 or len(arr2) > 0:
        if len(arr1) >0 and len(arr2) > 0:
            if arr1[0] <= arr2[0]:
                result.append(arr1.pop(0))
            else:
                result.append(arr2.pop(0))
        elif len(arr1) > 0:
            result.append(arr1.pop(0))

        elif len(arr2) > 0:
            result.append(arr2.pop(0))
    return result

def merge_sort(arr):
    # 만약 두 부분으로 나눌 수 없다면, 과정 없이 arr 그대로 반환
    if len(arr) == 1:
        return arr
    # 전체를 두 부분으로 나누는 부분
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    # 나뉜 두 분을 각각 merge_sort()를 실행
    left = merge_sort(left)
    right = merge_sort(right)
    # 각각에 대한 merge_sort()의 결과를 병합

    # 병합(merge) :두 배열에서 작은 순서대로 요소를 가져와서 새로운 배열 만들기
    # 병합한 배열 반환

    return merge(left, right)

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    result = merge_sort(arr)[N//2]
    print(f'#{tc} {result} {cnt}')

