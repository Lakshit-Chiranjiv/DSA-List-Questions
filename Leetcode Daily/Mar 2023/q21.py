class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c = 0
        zrs = []
        for i in nums:
            if i != 0 and c > 0:
                zrs.append(c)
                c = 0
            elif i == 0:
                c += 1
        if c > 0:
            zrs.append(c)

        ans = 0
        for i in zrs:
            ans += ((i*(i+1))//2)
        return ans
    

#intuition:
# 1. To find the number of subarrays filled with 0s, first we need to find set of contiguous 0s with the count of each set.
# 2. For example, if the array is [1,0,0,0,1,0,0,1,0,0,0,0,0,1], then the set of contiguous 0s is [3,2,5].
# 3. Now for each set, we can find the number of subarrays filled with 0s by using the formula n*(n+1)/2.
# 4. For example, if the set is [3,2,5], then the number of subarrays filled with 0s is 3*(3+1)/2 + 2*(2+1)/2 + 5*(5+1)/2 = 21.
# 5. This formula you can figure out by drawing a few examples starting with n=1 to n=5.
# 6. Finally, we can return the sum of all the subarrays filled with 0s.
# 7. Instead of storing the count of each set we can directly find the number of subarrays there for that set and add it to the answer.

#solution:
# 1. Initialize a variable c to 0 and a list zrs to store the set of contiguous 0s.
# 2. Iterate through the array and if the current element is not 0 and c is greater than 0, then we can append c to zrs and set c to 0.
# 3. If the current element is 0, then we can increment c by 1.
# 4. After the loop, if c is greater than 0, then we can append c to zrs to account for the last set of contiguous 0s.
# 5. Initialize a variable ans to 0.
# 6. Iterate through zrs and for each element, we can find the number of subarrays filled with 0s by using the formula n*(n+1)/2 and add it to ans.
# 7. Finally, we can return ans.