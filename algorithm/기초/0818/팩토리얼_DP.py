def fact(n):
    table[0] = 1
    for i in range(1, n+1):
        table[i] = i * table[i-1]

    return table[n]

"""
f(n) = n * f(n-1)

f(0) = 1
f(1) = 1
f(2) = 2 * 1 = n * f(1)
"""

n = int(input())
table = [0] * (n+1)
print(fact(n))

