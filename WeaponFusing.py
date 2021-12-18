# Question: Print the total number of weapon can be fuse
# weapon fused must be of same level
stage = int(input("Enter stage: "))
weapon = int(input("Enter number of weapons: "))
weaponLevel = [int(x) for x in input().split(' ')]
weaponLevel.sort()
i = 0
for x in range(len(weaponLevel)):
    if weaponLevel[0] == weaponLevel[1]:      # Weapon Level must be same
        fuse = weaponLevel[0] + 1
        weaponLevel.pop(0)
        weaponLevel.pop(0)
        weaponLevel.append(fuse)
        weaponLevel.sort()
        print(weaponLevel)     # Debugging purpose
        i = i + 1

print(i)        # Result
