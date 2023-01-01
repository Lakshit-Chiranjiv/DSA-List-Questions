# Print all the subsequences which sum to k

def printSubsequences(arr, k, output, index, sum):
    if index == len(arr):
        if sum == k:
            print(output)
        return
    printSubsequences(arr, k, output, index + 1, sum)
    output.append(arr[index])
    printSubsequences(arr, k, output, index + 1, sum + arr[index])
    output.pop()

arr = [1, 2, 3, 4, 5]

printSubsequences(arr, 5, [], 0, 0)