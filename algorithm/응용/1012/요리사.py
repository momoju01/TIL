def comb(cnt, idx, start):  # r개를 고르는 조합
    if cnt == find_num:  # 찾으려는 숫자만큼 찾은 경우
        cnt2 = 0
        for j in range(N):  # 고객 2의 재료 선택
            if j not in p1:
                p2[cnt2] = j
                cnt2 += 1
        cal()
    else:
        for i in range(start, N): # 고객 1의 재료 선택
            p1[idx] = i
            comb(cnt+1, idx+1, i+1)

def cal():
    global minV
    sum1 = 0  # 고객 1의 합
    sum2 = 0  # 고객 2의 합
    for i in range(N//2):
        for j in range(N//2):
            if i !=j :  # 같으면 제외
                sum1 += arr[p1[i]][p1[j]]
                sum2 += arr[p2[i]][p2[j]]
    if abs(sum1-sum2) < minV:
        minV = abs(sum1-sum2)
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 987654321
    p1 = [0]*(N//2)
    p2 = [0]*(N//2)
    find_num = N//2  # 선택해야할 개수

    comb(0, 0, 0)
    print(f'#{tc} {minV}')