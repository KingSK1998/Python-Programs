str1,str2 = input().split()
totalDistance = 0
for c in range(len(str1)):
    if str1[c] == str2[c]:
        totalDistance -= c
    else:
        totalDistance += c

print(totalDistance)