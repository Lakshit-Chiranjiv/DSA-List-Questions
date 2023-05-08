class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        
        sm = 0
        a = 0
        b = n-1
        for i in range(n):
            if a != b:
                sm += (mat[i][a] + mat[i][b])
            else:
                sm += (mat[i][a])
            a += 1
            b -= 1
        
        return sm

# intution:
# 1. As, it is a square matrix, so the sum of the diagonal elements will be the sum of the elements at the indices (0,0), (1,1), (2,2), ..., (n-1,n-1) and (0,n-1), (1,n-2), (2,n-3), ..., (n-1,0).
# 2. So, we can keep two pointers, one at (0,0) and the other at (0,n-1) and iterate over the matrix and keep moving the pointers towards each other.
# 3. If the pointers are not at the same index, then add the elements at the indices pointed by the pointers to the sum. Else, add the element at the index pointed by any of the pointers to the sum.
# 4. Return the sum.

# solution:
# 1. Initialize a variable sm to 0.
# 2. Initialize two variables a and b to 0 and n-1 respectively, where n is the number of rows or columns in the matrix.
# 3. Iterate over the matrix and add the elements at the indices pointed by the pointers a and b to the sum sm.
# 4. Increment a and decrement b.
# 5. Return sm.

# Time Complexity: O(n) as we are iterating only over the rows of the matrix.

# Space Complexity: O(1) as we are not using any extra space.