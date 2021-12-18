def func(n, k, q):
    arr = [0]
    for i in range(2, n):
        arr.append(k + sum([i for i in range(2, i-1)]))
    p = []
    x = []
    for i in arr:
        if i <= q:
            x.append(i)
    for i in range(len(q)):
        p.append(max(x))
    return p


print(func(3, 2, [2, 8]))
print(func(3, 2, [5, 1]))