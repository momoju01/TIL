def f(i, N, K): # 합이 K인 부분집합을 출력
    global cnt1
    cnt1 += 1
    if i==N: # 부분집합 생성완료
        s = 0
        for j in range(N):
            if bit[j]==1:
                s += A[j]
        if s == K: # 합이 찾는 값이면
            print(bit, end= ' ')
            for j in range(N):
                if bit[j]==1:
                    print(A[j], end =' ')  # 부분 집합 출력
            print()
    else:
        bit[i] = 1
        f(i+1, N, K)
        bit[i] = 0
        f(i+1, N, K)

def f2(i, N, K, S, RS):
    global cnt2
    cnt2 += 1
    if S==K:
        print(bit, end=' ')
        for j in range(N):
            if bit[j] == 1:
                print(A[j], end=' ')  # 부분 집합 출력
        print()
    elif i==N:
        return
    elif S > K:
        return
    elif S+RS < K:
        return
    else:
        bit[i] = 1
        f2(i + 1, N, K, S+A[i], RS-A[i])
        bit[i] = 0
        f2(i + 1, N, K, S, RS-A[i])

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0]*10
cnt1 = 0
f(0, 10, 10)
print(cnt1)
cnt2 = 0
f2(0, 10, 25, 0, sum(A))
print(cnt2)