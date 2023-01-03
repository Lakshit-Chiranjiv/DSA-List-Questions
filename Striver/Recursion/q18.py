# print all permutations of a string/array

def permutations(arr, elementsMap, temp, ans):
    if len(temp) == len(arr):
        ans.append(temp[:])
        return
    for i in range(len(arr)):
        if elementsMap[arr[i]] == 0:
            continue
        temp.append(arr[i])
        elementsMap[arr[i]] -= 1
        permutations(arr, elementsMap, temp, ans)
        temp.pop()
        elementsMap[arr[i]] += 1

arr = [1, 2, 3]
elementsMap = {}

for i in arr:
    if i in elementsMap:
        elementsMap[i] += 1
    else:
        elementsMap[i] = 1

ans = []

permutations(arr, elementsMap, [], ans)
print(ans)
