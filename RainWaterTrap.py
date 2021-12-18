# Given n non-negative integers representing an elevation map
# where the width of each bar is 1, compute how much water it
# can trap after raining.

# Input: height = {0,1,0,2,1,0,1,3,2,1,2,1};
# Output: 6 

# Input: height = {4,2,0,3,2,5};
# Output: 9

# Author: Shivam Kashyap

# Solution with list as height
# def solution(height):
#     max = 0
#     curr = 0
    
#     for i in height:
#         # print("i=",i)
#         if max < i:
#             max = i
#             # print("max=",max)
#             curr = curr + max
#             # print("curr=",curr)
    
#     # print("sol=",curr)
#     return curr

def solution(height):
    maxHeight = max(height)
    maxWidth = len(height)-1
    heatmap = []

    for x in range(maxHeight):
        row = []
        for y in range(maxWidth):
            col = []
            for m in range(maxHeight):
                if m < maxHeight-height[x]:
                    col.append(0)
                else:
                    col.append(1)
            row.append(col)
        heatmap.append(row)

    displayMatrix(heatmap)

    return

def displayMatrix(data):
    for i in data:
        for j in i:
            # print('.' if j==0 else '*', end=' ')
            print(j, end=' ')
        print("\n")

# Main
h1 = [0,1,0,2,1,0,1,3,2,1,2,1]
h2 = [4,2,0,3,2,5]

print("Case 1:\n")
print("Success" if solution(h1) == 6 else "Fail")
print("\n\nCase 2:\n")
print("Success" if solution(h2) == 9 else "Fail")