m = int(input())
t = list(map(int, input().split(',')))
matrix = []
index = 0
for r in range(m):
    tc = []
    for c in range(index, index+5):
        tc.append(int(t[c]))
    index += 5
    matrix.append(tc)

for i in matrix:
    for j in matrix[i]:
        print(matrix[i][j] + " ")
    print("\n")