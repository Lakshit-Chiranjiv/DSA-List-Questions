# kth permutation sequence for a set of n numbers

n = 4
k = 9

ans = ""
nums = [i for i in range(1, n+1)]
fact = 1
for i in range(1, n):
    fact *= i

k -= 1

while True:
    ans += str(nums.pop(k // fact))
    if not nums:
        break
    k %= fact
    fact //= len(nums)

print(ans)


