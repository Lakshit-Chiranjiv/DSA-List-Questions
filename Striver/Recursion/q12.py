# Print a single subsequence which sums to k

def printSubsequences(arr, k, output, index, sum):
    if index == len(arr):
        if sum == k:
            print(output)
            return True
        return False
    if printSubsequences(arr, k, output, index + 1, sum) == True:
        return True
    output.append(arr[index])
    if printSubsequences(arr, k, output, index + 1, sum + arr[index]) == True:
        return True
    output.pop()
    return False

arr = [1, 2, 3, 4, 5]
printSubsequences(arr, 5, [], 0, 0)