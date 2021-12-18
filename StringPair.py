def num2words(num):
    ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    numString = ""
    if num == 0: numString = "zero"
    elif num == 100: numString = "hundred"
    else:
        if num <= 9:
            numString = ones[num-1]
        elif num >= 11 and num <=19:
            numString = teens[num%10 - 1]
        elif num%10 == 0:
            numString = tens[int(num/10)-1]
        else:
            numString = tens[int(num/10) - 1] + " " + ones[num%10 - 1]
    return numString

def MrString(num):
    sum = 0
    for n in num:
        count = 0
        string = num2words(n)
        for i in string:
            if i in 'aeiou':
                count += 1
        sum += count
    return sum

if __name__ == "__main__":
    n = int(input())
    numbers = [int(x) for x in input().split()][:n]
    D = MrString(numbers)
    count = 0
    for x in numbers:
        for y in numbers:
            if x+y == D:
                count+=1
    print(num2words(int(count/2)))