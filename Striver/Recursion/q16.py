# print the sum of all the subsets of an array in ascending order

def subsetSum(arr, index, sum, ans):
    if index == len(arr):
        ans.append(sum)
        return
    subsetSum(arr, index+1, sum, ans)
    subsetSum(arr, index+1, sum+arr[index], ans)

arr = [1, 2, 3]
ans = []
subsetSum(arr, 0, 0, ans)
ans.sort()
print(ans)