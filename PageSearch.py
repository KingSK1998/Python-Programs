def fetchItemsToDisplay(items, sortParameter, sortOrder, itemsPerPage, pageNumber):
    if sortParameter == 0:
        if sortOrder == 0:
            items.sort(key = lambda x: x[0])
        if sortOrder == 1:
            items.sort(key = lambda x: x[0], reverse = True)
    elif sortParameter == 1:
        if sortOrder == 0:
            items.sort(key = lambda x: x[1])
        if sortOrder == 1:
            items.sort(key = lambda x: x[1], reverse = True)
    elif sortParameter == 2:
        if sortOrder == 0:
            items.sort(key = lambda x: x[2])
        if sortOrder == 1:
            items.sort(key = lambda x: x[2], reverse = True)
    pageItems = []
    l = []
    for pn in range(pageNumber):
        l = []
        for p in range(itemsPerPage)
            l.append(items[p][sortParameter])
        pageItems.append(l)
    return pageItems

if __name__ == '__main__':
    items_rows = int(input().strip())
    items_columns = int(input().strip())
    items = []
    for _ in range(items_rows):
        items.append(input().rstrip().split())
    sortParameter = int(input().strip())
    sortOrder = int(input().strip())
    itemsPerPage = int(input().strip())
    pageNumber = int(input().strip())
    result = fetchItemsToDisplay(items, sortParameter, sortOrder, itemsPerPage, pageNumber)
    print('\n'.join(result))
    print('\n')
