limits = [int(x) for x in input().split(' ')]
querries = []
for i in range(limits[1]):
    querries.append([])
    querries[i] = [int(i) for i in input().split(' ')]

array = []

for querry in querries:
    sum = 0
    if querry[0] == 1:
        x = querry[1]
        y = querry[2]
        for i in range(x, y):
            array[i].append(array[i] + i*(i+1))
        print(array)
    if querry[0] == 2:
        i = querry[1]  # 1
        j = querry[2]  # 10
        while(i <= j):
            sum = sum + array[i-1]
            print("i: " + str(i)
                  + "     j: " + str(j)
                  + "     sum: " + str(sum)
                  + "     arr: " + str(array[i-1]))
            i = i + 1
        print("querry: " + str(sum % 109))
