# babygin 완전탐색으로

def perm(n, k):  # Permutation(순열), n: 순열의 길이, k: 결정할 위치
    global ans
    if n == k:
        # 베이비진 판정
        run = 0
        tri = 0
        if arr[0]+1 == arr[1] and arr[1]+1 == arr[2]:  #왼쪽 절반이 run인 경우
            run += 1
        if arr[0] == arr[1] == arr[2]:
            tri += 1
        if arr[3]+1 == arr[4] and arr[4]+1 == arr[5]:   # 오른쪽 절반이 run인 경우
            run += 1
        if arr[3] == arr[4] == arr[5]:
            tri += 1
        if run + tri == 2:
            ans = 'Baby-Gin'

    else:
        for i in range(n):
            if u[i] == 0:    # 사용 안했으면
                u[i] = 1    # 사용 표시
                p[k] = arr[i]
                perm(n, k+1)
                u[i] = 0   # 사용 안 한 걸로

ans = 'Not Baby-Gin'
p = [0] * 6
u = [0] * 6
arr = list(map(int, input()))
perm(6, 0)

print(ans)



