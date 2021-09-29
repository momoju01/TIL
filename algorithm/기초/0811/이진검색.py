def binarySearch(a, key):
    start = 0
    end = len(a)-1
    while start <= end :
        middle = (start + end)//2
        if a[middle] == key:  # 검색 성공
        	return middle
        elif a[middle] > key:  # 중앙 원소 값이 목표 값보다 크면
            end = middle - 1   # 목표 값이 더 아래이니 왼쪽에서만 검색
        else:
            start = middle + 1
    return -1  # 검색 실패


arr = [2, 4, 7, 9, 11, 19, 23]
print(binarySearch(arr, 11))
print(binarySearch(arr, 10))