numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for T in range(1, T + 1):
    tc, N = input().split()  # '#' 포함한 문자열 그대로 출력 예정

    # 문자열 리스트로 변환
    inputV = input()
    str_list = list(inputV.split())
    count = [0] * 10  # 순서대로 출력하면 되니 각 원소의 갯수로 접근해 세기

   for i in range(len(str_list)):  # 전체 리스트
        for j in range(10):  # numbers 리스트
            if str_list[i] == numbers[j]:  # 값 같으면
                count[j] += 1  # count 리스트의 해당하는 인덱스에 값 추가

    # 순서대로 출력하기

    print(tc)
    for i in range(10):
        print((numbers[i] + ' ') * count[i], end='')
    print()