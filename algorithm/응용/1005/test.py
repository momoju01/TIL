# 끝나는 시간이 빠른 순서대로 정렬하기 (14 -> 18 -> 20 -> 23 -> 24)
for i in range(0, N - 1):
    minidx = i
    for j in range(i + 1, N):
        if A_list[j][1] < A_list[minidx][1]:
            minidx = j
    A_list[i], A_list[minidx] = A_list[minidx], A_list[i]
# print(A_list)   #[(4, 14), (8, 18), (17, 20), (20, 23), (23, 24)]

S_list = []  # 선택된 활동들의 집합
S_list.append(A_list[0])  # 첫번째 활동은 무조건 선택 가능하므로 어펜드
j = 0  # 0번째 인덱스로 초기화 / j는 S_list에 선택된 활동의 마지막인덱스
for i in range(1, N):  # 0번째 인덱스 제외 A_list에 남은 활동에 대해
    if A_list[i][0] >= S_list[j][
        1]:  # 현재 S_list에 선택된 활동의 끝나는 시간이(#S_list[j][1]) 다음 고려하는 A_list에 대기중인 활동의 시작시간(A_list[i][0])과 같거나 이르면
        S_list.append(A_list[i])  # A_list의 i번째 튜플 전체를 선택된 활동 리스트(S_list)에 넣어줌
        j += 1  # S_list에 선택된 활동의 마지막인덱스를 하나 밀어줌(하나 추가되었으니)
# print(S_list, j)
print(f'#{tc} {j + 1}')