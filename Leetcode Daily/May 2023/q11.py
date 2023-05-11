class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        @cache
        def solve(i,j):
            if i >= m or j >= n:
                return 0
            mx = 0
            for z in range(j,n):
                if nums1[i] == nums2[z]:
                    mx = max(mx,1+solve(i+1,z+1))

            mx = max(mx,solve(i+1,j))

            return mx

        return solve(0,0)

# intuition:
# 1. If one element connects to some equal in the other array then the indexes previous to that element in both the arrays are of no more use to us.
# 2. We can use dp by keeping a pointer in both the arrays and then we can either connect an equal element or we can skip the element in the first array.

# solution:
# 1. Take the length of both the arrays in variables m and n.
# 2. Define a function solve(i,j) which returns the maximum number of lines that can be drawn withou crossing each other if we start from index i in the first array and index j in the second array.
# 3. If i >= m or j >= n then return 0.
# 4. Keep a variable mx to store the maximum number of lines that can be drawn.
# 5. Loop over from j to n and check if nums1[i] == nums2[z] then update mx = max(mx,1+solve(i+1,z+1)).
# 6. Update mx = max(mx,solve(i+1,j)) to account for the case when we skip the element in the first array.
# 7. Return mx.