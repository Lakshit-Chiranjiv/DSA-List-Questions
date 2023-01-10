# maximum subarray length with sum divisible by k

def subarraySum(arr,n,k):
    mp = {}

    mod_arr = []
    mx_len = 0
    curr_sum = 0

    for i in range(n):
        curr_sum += arr[i]
        mod_arr.append(curr_sum%k)

        if mod_arr[i] == 0:
            mx_len = i+1
        elif mod_arr[i] in mp:
            mx_len = max(mx_len,i-mp[mod_arr[i]])
        else:
            mp[mod_arr[i]] = i

    return mx_len

def subarraySum2(arr,n,k):
    mp = {}

    curr_sum = 0
    mx_len = 0

    for i in range(n):
        curr_sum += arr[i]

        mod = curr_sum%k

        if mod == 0:
            mx_len = i+1
        elif mod in mp:
            mx_len = max(mx_len,i-mp[mod])
        else:
            mp[mod] = i
    return mx_len

arr = [2,7,6,1,4,5]
n = len(arr)
k = 3

print(subarraySum(arr,n,k))
print(subarraySum2(arr,n,k))