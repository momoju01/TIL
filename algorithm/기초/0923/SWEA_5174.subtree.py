def f(n): # 순회하는 함수
    global cnt
    if n:
        cnt += 1
        f(ch1[n])
        f(ch2[n])

# 추가... 뭔내용인지 모름
def f2(n):
    if n == 0:
        return 0
    else:
        r1 = f2(ch1[n])
        r2 = f2(ch2[n])
        return r1 + r2 + 1

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E+1 # 1번부터 V 번까지 정점 번호
    ch1 = [0]*(V+1)  # 자식 1 혹은 왼쪽 자식, 부모를 인덱스로 자식 번호 저장
    ch2 = [0]*(V+1)  # 자식 2 혹은 오른쪽 자식
    arr = list(map(int, input().split()))
    for i in range(E):
        n1, n2 = arr[i*2], arr[i*2+1] # 부모n1, 자식 n2
        if ch1[n1] == 0:  # 자식 1이 아직 없으면
            ch1[n1] = n2

        else:
            ch2[n1] = n2
    cnt= 0
    f(N)
    print(f'#{tc} {cnt}')



