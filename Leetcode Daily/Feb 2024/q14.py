class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = []
        n = []
        for i in nums:
            if i >= 0:
                p.append(i)
            else:
                n.append(i)
        ans = []
        x = 0
        y = 0
        for i in range(len(nums)):
            if i%2 == 0:
                ans.append(p[x])
                x += 1
            else:
                ans.append(n[y])
                y += 1
        return ans

# Time complexity: O(n)
# Space complexity: O(n)
    
# We create two lists, one for positive numbers and one for negative numbers. We then iterate through the list of numbers and add the positive numbers to the answer list at even indices and the negative numbers at odd indices. We then return the answer list.