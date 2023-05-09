class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res
        m, n = len(matrix), len(matrix[0])
        hashset = set()
        
        def dfs(i, j, order):
            if i < 0 or i >= m or j < 0 or j >= n or (i,j) in hashset:
                return
            res.append(matrix[i][j])
            hashset.add((i, j))
            dirs = [[i, j+1], [i+1, j], [i, j-1], [i-1, j]]
            k = order
            while k < 4:
                dfs(dirs[k][0], dirs[k][1], k)
                k += 1
            k = 0
            while k < order:
                dfs(dirs[k][0], dirs[k][1], k)
                k += 1
        
        dfs(0, 0, 0)
        return res
    
# intution:
# 1. We can use a hashset to keep track of the visited indices and a variable order to keep track of the direction in which we are moving.
# 2. We can use a dfs approach to traverse the matrix in a spiral order and add the elements to the result list.
# 3. Recusively call the dfs function with the current indices and the current order and add the element at the current indices to the result list.

# solution:
# 1. Initialize a variable res to an empty list.
# 2. If the matrix is empty, return res.
# 3. Initialize two variables m and n to the number of rows and columns in the matrix respectively.
# 4. Initialize a hashset to keep track of the visited indices.
# 5. Define a dfs function which takes the current indices and the current order as parameters.
# 6. If the current indices are out of bounds or the current indices are already visited, return.
# 7. Add the element at the current indices to the result list res and add the current indices to the hashset.
# 8. Define a list dirs which contains the directions in which we can move from the current indices.
# 9. Initialize a variable k to the current order.
# 10. While k is less than 4, recursively call the dfs function with the indices pointed by the kth element of dirs and k as parameters and increment k by 1 in each iteration.
# 11. Initialize k to 0.
# 12. While k is less than the current order, recursively call the dfs function with the indices pointed by the kth element of dirs and k as parameters and increment k by 1 in each iteration. This is done to cover the case when we are moving in the same direction as the previous iteration.
# 13. Call the dfs function with the indices (0,0) and 0 as parameters.
# 14. Return res.