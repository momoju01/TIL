def nCr(n, r, s, k):  # n개에서 r개를 고르는 조합, s:선택할 수 있는 구간의 시작, k 고른 갯수
    if k == r:
        print(*comb)
    else:
        for i in range(s, n-r+k+1):
            comb[k] = i
            nCr(n, r, i+1, k+1)

N = 4
R = N//2
comb = [0]*R
nCr(N, R, 0, 0)