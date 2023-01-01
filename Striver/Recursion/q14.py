# print all combination sum of array elements which sum to target where each element can be used any number of times

def combinationSum(arr, target, index, path):
    if index == len(arr):
        if target == 0:
            print(path)
        return
    if target - arr[index] >= 0:
        combinationSum(arr, target - arr[index], index, path + [arr[index]])
    combinationSum(arr, target, index + 1, path)

arr = [2, 3, 5, 7]
combinationSum(arr, 7, 0, [])