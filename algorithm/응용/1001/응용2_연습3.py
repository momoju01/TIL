a = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(a)

for i in range(1, 1<<n):
    s = 0
    subset = []
    for j in range(n):
        if i &(1<<j):
            s += a[j]
            subset.append(a[j])
    if s==0:
        print(subset)