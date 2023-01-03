# return all possible subsets of an array with no duplicates

def subsets(arr, index, temp, ans):
    ans.append(temp[:])
    for i in range(index, len(arr)):
        if i > index and arr[i] == arr[i-1]:
            continue
        temp.append(arr[i])
        subsets(arr, i+1, temp, ans)
        temp.pop()

arr = [1, 2, 2]
arr.sort()
ans = []
temp = []
subsets(arr, 0, temp, ans)
print(ans)