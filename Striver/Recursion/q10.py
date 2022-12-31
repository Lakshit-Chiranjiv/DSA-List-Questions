# print all the subsequence of an array using recursion

def subsequence(arr, n, sub):
    if n == len(arr):
        print(sub)
        return
    subsequence(arr, n + 1, sub)
    subsequence(arr, n + 1, sub + [arr[n]])

arr = [1, 2, 3]
subsequence(arr, 0, [])

# print all the subsequence of a string using recursion

def subsequence(s, n, sub):
    if n == len(s):
        print(sub)
        return
    subsequence(s, n + 1, sub)
    subsequence(s, n + 1, sub + s[n])

s = "abc"
subsequence(s, 0, "")
