def CalulateDistinctElements(input1, input2, input3):
    return list(sorted(set(input1+input2+input3)))


def CheckingCarry(input1, input2, input3):
    x = len(input1)
    y = len(input2)
    z = len(input3)
    if (z == x + 1) or (z == y + 1):
        return True
    return False


def AssignCarryToSolution(input3):
    assign1 = input3[0]
    return assign1


def CalculateNextValue(s1, s2, s3, solution):
    i = 0
    while i <= len(s3):
        if len(s1) == len(s3):
            break
        else:
            s1 = "_" + s1
        i += 1
    i = 0
    while i <= len(s3):
        if len(s2) == len(s3):
            break
        else:
            s2 = "_" + s2
        i += 1


def MaxLength(input1, input2):
    return len(input1) if len(input1) >= len(input2) else len(input2)


if __name__ == "__main__":
    input1 = "SEND"
    input2 = "MORE"
    input3 = "MONEY"
    # Find total number of distinct characters
    disctinctCharacters = CalulateDistinctElements(input1, input2, input3)

    if len(disctinctCharacters) <= 10:
        # make a nested list as ll[[character, assigned_Number]]
        solution = {i: 10 for i in disctinctCharacters}

        if CheckingCarry(input1, input2, input3):
            solution[AssignCarryToSolution(input3)] = 1
            CalculateNextValue(input1, input2, input3, solution)
        else:
            print("Carry not Generated")

        maxLength = MaxLength(input1, input2)

        print(solution)

    else:
        print("Solution Not Possible XD")
