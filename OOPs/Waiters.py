# Base Class
class Table:
    tableNo = 0
    waiterName = ""
    status = ""

    def __init__(self, table, waiter, state):
        self.tableNo = table
        self.waiterName = waiter
        self.status = state

# Methods not belong to any class : (list of table)    
def findWaiterWiseTotalNoOfTables(tables):
    waiterCount = {}
    for table in tables:
        if not table.waiterName in waiterCount:
            waiterCount[table.waiterName] = 1
        else:
            waiterCount[table.waiterName] += 1
    return waiterCount

def findWaiterNameByTableNo(tables, tableNumber):
    waiterName = "none"
    for table in tables:
        if tableNumber == table.tableNo:
            waiterName = table.waiterName
    return waiterName

# Main Section
if __name__ == "__main__":
    numberOfTables = int(input())
    tables = []
    for i in range(numberOfTables):
        tableNo = int(input())
        waiterName = input()
        status = input()
        table = Table(tableNo, waiterName, status)
        tables.append(table)

    waiters = findWaiterWiseTotalNoOfTables(tables)
    for key,value in sorted(waiters.items()):
        print("{}-{}".format(key, value))

    tableNumber = int(input())
    foundName = findWaiterNameByTableNo(tables, tableNumber)
    if foundName != 'none':
        print(foundName)
    else:
        print("No Table Found")