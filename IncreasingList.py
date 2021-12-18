# from math import *
# print(floor(3.7))
# print(ceil(3.7))
# print(sqrt(36))

# name = input("Enter your name: ")
# print(name)

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = int(num1) + float(num2)

# def generateList(startvalue, endvalue):
#     print([x for x in range(startvalue, startvalue+3)])
#     print([x for x in range(endvalue, startvalue, -1)][:5:])
#     print([x for x in range(startvalue, endvalue, 4)])
#     print([x for x in range(endvalue, startvalue-1, -2)])

# generateList(10, 16)

# * Removes every single element > val from our list
# i = 0
# while i != len(self.myList):
#     if (self.myList[i] > val):
#         # index = self.myList.index(element)      #? Inbuilt Function
#         self.myList.pop(i)                  #? Inbuilt Function
#         i = 0
#     else:
#         i = i + 1


class IncreasingList:
    # Strict Typing
    myList = list

    def __init__(self):
        self.myList = []

    def append(self, val):  # ? Class Function
        for i in range(len(self.myList)-1, -1, -1):
            if (self.myList[i] > val):
                self.myList.pop(i)
        self.myList.append(val)

    def pop(self):
        return self.myList.pop()

    def __len__(self):
        return len(self.myList)


lst = IncreasingList()

print(lst.__len__())
lst.append(2)
lst.append(4)
lst.append(5)
print(lst.__len__())
lst.append(2)
print(lst.__len__())
lst.pop()
print(lst.__len__())
