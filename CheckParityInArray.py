def FillArrayWithLengths(message):
    arr = []
    x = message.split()
    if len(x) <= 25:
        for i in range(0, len(x), 5):
            temp = []
            for j in range(i, i+5):
                if j < len(x):
                    temp.append(len(x[j]))
                else:
                    temp.append(0)
            arr.append(temp)
    return arr
            
def CalRowSum(arr):
    return [sum(x) for x in arr]

def CalColumnSum(arr):
    colSum = []
    for j in range(5):
        ss = 0
        for i in range(5):
            ss += arr[i][j]
        colSum.append(ss)
    return colSum


def CalParity(arr, r, c):
    return sum(r)+sum(c)

if __name__ == "__main__":
    message = input()
    arr = FillArrayWithLengths(message)
    r = CalRowSum(arr)
    c = CalColumnSum(arr)
    parity = CalParity(arr, r, c)
    print(parity)