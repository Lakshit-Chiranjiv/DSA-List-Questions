# print all possible combinations of r elements in a n-size array

def combinationUtil(arr, n, r, index, data, i):
    if index == r:
        for j in range(r):
            print(data[j], end = " ")
        print()
        return

    if i >= n:
        return

    # current is included, put next at next location in data
    data[index] = arr[i]

    # current is included, put next at next location
    combinationUtil(arr, n, r, index + 1, data, i + 1)

    # current is excluded, replace it with next (Note that i+1 is passed, but index is not changed)
    combinationUtil(arr, n, r, index, data, i + 1)

def printCombination(arr, n, r):
    data = [0] * r
    combinationUtil(arr, n, r, 0, data, 0)

arr = [1, 2, 3, 4, 5]
r = 3
n = len(arr)
printCombination(arr, n, r)