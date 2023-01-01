# print the count of subsequences which sums to k

def countSubsequences(arr, k, index, sum):
    if index == len(arr):
        if sum == k:
            return 1
        return 0
    count = countSubsequences(arr, k, index + 1, sum)
    count += countSubsequences(arr, k, index + 1, sum + arr[index])
    return count

arr = [1, 2, 3, 4, 5]
print(countSubsequences(arr, 5, 0, 0))