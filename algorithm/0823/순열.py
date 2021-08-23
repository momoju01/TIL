# 만들 때마다 순열 출력하기 3개 다 사용해서

def f(i, N):    #P[i]의 값을 결정하는 함수
    if i == N:  # 배열을 벗어났다 (크기와 인덱스가 일치)
        print(P)
    else:
        for j in range(i, N):  # P[i] <-> P[j] 자리 교환
            P[i], P[j] = P[j], P[i]
            f(i+1, N)
            P[i], P[j] = P[j], P[i]

P = [1, 2, 3]
f(0, 3)