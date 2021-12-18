friends = ["a", "b", "crowd", 2, False]

print(friends)
print(friends[0])
print(friends[1:])
luckyNums = [4, 8, 15, 16, 23, 42]
friend2 = friends.copy()
friends.extend(luckyNums)
friends.append("roahna")
friends.insert(1, "kelly")
friends.remove("kelly")
friends.clear()
luckyNums.pop()
print(luckyNums.index(4))
print(luckyNums.count(4))
print(luckyNums.sort())
