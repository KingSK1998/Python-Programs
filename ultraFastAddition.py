while True:
    com = input().split()
    if len(com) == 0:
        break
    else:
        print(int(com[0]) + int(com[1]))