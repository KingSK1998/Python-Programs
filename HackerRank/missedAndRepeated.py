arr = list(map(int, input().split()))
arr.sort()
size = len(arr)
repeat = 0
miss = 0
for i in range(size):
    if arr[i] == arr[i-1]:
        repeat = arr[i]
    if i+1 not in arr:
        miss = i+1
print(miss, repeat)
print(abs(miss - repeat))