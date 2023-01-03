# return all permutations of a string/array - recursion swapping approach

def permute(arr,idx,ans):
    if idx == len(arr):
        ans.append(arr[:])
        return
    for i in range(idx,len(arr)):
        arr[idx],arr[i] = arr[i],arr[idx]
        permute(arr,idx+1,ans)
        arr[idx],arr[i] = arr[i],arr[idx]

arr = [1,2,3]
ans = []
permute(arr,0,ans)
print(ans)