def f(n, arr):
    n = n - 1
    sum = 0
    for i in range(n):
        if (0 <= i and i <= (n-1)) and (arr[i] & arr[n] > 0):
            sum += 0
        else:
            sum += arr[n] ^ arr[i]
    return sum

def g(n, arr):
    n = n - 1
    sum = 0
    for i in range(n):
        if (0 <= i and i <= (n-1)) and (arr[i] & arr[n] > 0):
            sum += 0
        else:
            sum += arr[n] ^ arr[i]
    return sum

def solve(n, arr):
    return ((f(n, arr) + g(n, arr)) % (pow(10, 9)+7))

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    out_ = solve(n, arr)
    print(out_)