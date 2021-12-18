def printMaxSubSquare(M): 
    R = len(M) # no. of rows in M[][] 
    C = len(M[0]) # no. of columns in M[][] 
  
    S = [[0 for k in range(C)] for l in range(R)] 
    # here we have set the first row and column of S[][] 
  
    # Construct other entries 
    for i in range(1, R): 
        for j in range(1, C): 
            if (M[i][j] == 1): 
                S[i][j] = min(S[i][j-1], S[i-1][j], 
                            S[i-1][j-1]) + 1
            else: 
                S[i][j] = 0
      
    # Find the maximum entry and 
    # indices of maximum entry in S[][] 
    max_of_s = S[0][0] 
    max_i = 0
    max_j = 0
    for i in range(R): 
        for j in range(C): 
            if (max_of_s < S[i][j]): 
                max_of_s = S[i][j] 
                max_i = i 
                max_j = j 
    return max_of_s * max_of_s
    
string = input()
string = string.replace("[", "")
string = string.replace("]", "")
string = string.replace(",", "")
string = string.replace('"', '')
M = []
x = ""
for c in string:
    if c != ' ':
        x += c
    else:
        M.append(list(x))
        x = ""
M.append(list(x))
print(printMaxSubSquare(M))