def printParenthesis(str, n):
    if n > 0:
        paren(str, 0, n, 0, 0)
    return

def paren(str, pos, n, open, close):
    if close == n:
        for i in str:
            print(i, end = "")
        print()
        return
    else:
        if open > close:
            str[pos] = '}'
            paren(str, pos+1, n, open, close+1)
        if open < n:
            str[pos] = '{'
            paren(str, pos+1, n, open+1, close)

n = int(input("Enter n: "))
str = [""] * 2 * n
printParenthesis(str, n)