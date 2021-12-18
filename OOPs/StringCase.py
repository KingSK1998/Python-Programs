ss = input()
u = 0
l = 0
for c in ss:
    if c.isupper():
        u = u + 1
    if c.islower():
        l = l + 1

print("Upper case characters :", u)
print("Upper case characters :", l)