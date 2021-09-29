def fibo(n):
    if n < 2:
        return n

    t1 = fibo(n-1)
    t2 = fibo(n-2)
    return t1 + t2


def fibo_m(n):
    # if n < 2:
    #     memo[n] = n
    #     return n
    if n >= and memo[n] == 0:  # memo 에 저장된 것이 있으면 :
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]


n = 10
memo = [0] * (n +1)
memo[0] = 0
memo[1] = 1