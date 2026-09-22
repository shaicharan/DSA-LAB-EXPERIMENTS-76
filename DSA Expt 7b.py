def selectionSort(itemsList):
    n = len(itemsList)
    for i in range(n - 1):
        minValueIndex = i
        for j in range(i + 1, n):
            if itemsList[j] < itemsList[minValueIndex]:
                minValueIndex = j
        if minValueIndex != i:
            temp = itemsList[i]
            itemsList[i] = itemsList[minValueIndex]
            itemsList[minValueIndex] = temp
    return itemsList
el = [29, 6, 37, 45, 5]
print("Unsorted list... ")
print(el)
print("Sorted list")
print(selectionSort(el))
