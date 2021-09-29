DATA = [0, 4, 1, 3, 1, 2, 4, 1]
N = len(DATA)
K = 5
# 목표 counts = [1, 3, 1, 1, 4]
COUNTS = [0] * 5  # 데이터 개수 종류만큼 잡기
TEMP = [-1] * N


# for i in range(N):
#     pos = DATA[i]
#     COUNTS[pos] += 1

for pos in DATA:
    COUNTS[pos] += 1

# 0, 1 -> 1
# 1, 2 -> 2
for i in range(K-1):
    COUNTS[i+1] = COUNTS[i] + COUNTS[i+1]


# 끝에서부터 데이터 입력하면서 오기 (앞부터 안 하는 건 정렬 상태 그대로 유지하기 위해)
for d in DATA:
    # COUNTS[d] -= 1
    # pos = COUNTS[d]
    # TEMP[pos] = d

    COUNTS[d] -= 1
    TEMP[COUNTS[d]] = d


print(COUNTS)
