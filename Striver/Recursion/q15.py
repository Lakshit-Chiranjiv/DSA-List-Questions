# print all combination sum of array elements which sum to target where each element can be used only once in a combination and answer set should not contain duplicate combinations

def combinationSum2(arr, target, index, ans, temp):
    if target == 0:
        ans.append(temp[:])
        return
    if target < 0:
        return
    for i in range(index, len(arr)):
        if i > index and arr[i] == arr[i-1]:
            continue
        temp.append(arr[i])
        combinationSum2(arr, target-arr[i], i+1, ans, temp)
        temp.pop()


arr = [10, 1, 2, 7, 6, 1, 5]
target = 8
arr.sort()
ans = []
temp = []
combinationSum2(arr, target, 0, ans, temp)
print(ans)