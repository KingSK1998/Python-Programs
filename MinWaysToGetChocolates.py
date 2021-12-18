testCases = int(input())
chocolates = [ ]
for x in range(testCases):
    chocolates.append(int(input()))

for num in chocolates:          # num = element of list
    day  = 0                    # reset day for new number
    while num >= 0:             # if num is poitive or it become 0
        if day == 0:            # If day is 0 then make it day 1
            num = num - 1       # consume no more than 1 chocolate on first day (or else spanks by mom)
            day = day + 1       # day completed successfully XD
        else:
            
            day = day + 1       # increment day until its not last day
    print(day)                  # number ends now it's time to print it     
