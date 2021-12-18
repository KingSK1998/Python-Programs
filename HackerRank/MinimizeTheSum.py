A = list(map(int, input().split()))
temp = A
num1 = ""
num2 = ""
while len(temp) != 0:
    temp.sort()
    if len(temp)!=1:
        min1 = temp[0]
        min2 = temp[1]
        temp.remove(min1)
        temp.remove(min2)
        num1 += str(min1)
        num2 += str(min2)
    else:
        x = temp[0]
        tn1 = num1
        tn2 = num2
        if (int((tn1 + str(x))) < int((tn2 + str(x)))):
            num1 += str(x)
        else:
            num2 += str(x)
        temp.remove(x)

print((int(num1) + int(num2)))