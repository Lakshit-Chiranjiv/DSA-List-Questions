class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        p = 1
        l = 0
        for r in range(len(nums)):
            p *= nums[r]
            while l <= r and p >= k:
                p = p // nums[l]
                l += 1
            ans += (r-l+1)
        return ans
    
# 713. Subarray Product Less Than K
# Time Complexity: O(n)
# Space Complexity: O(1)
    
# We maintain a pointer l which denotes the left end of the window and a pointer r which denotes the right end of the window. We maintain a variable p which denotes the product of the elements in the window. We iterate through the list and keep multiplying the product with the current element. If the product exceeds k, we divide the product by the element at the left end of the window and increment l. We keep track of the number of subarrays whose product is less than k and return the count.