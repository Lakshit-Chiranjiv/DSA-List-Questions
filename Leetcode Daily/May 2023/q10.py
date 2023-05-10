class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for k in range(n)]
        mat = [[tuple([i, j]) for j in range(n)] for i in range(n)]

        def spiralOrder(matrix):
            return matrix and list(matrix.pop(0)) + spiralOrder(list(zip(*matrix))[::-1])
        
        order = spiralOrder(mat)
        
        for ind, v in enumerate(order):
            ans[v[0]][v[1]] = ind+1
            
        return ans
    
# intution:
# 1. There will be a matrix which will contain the indices of the elements in the spiral order.
# 2. We can use the spiralOrder function from the previous problem to get the indices of the elements in the spiral order.
# 3. We can use the indices from the spiralOrder function to fill the matrix with the numbers from 1 to n*n using a for loop and enumerate function.

# solution:
# 1. Initialize a variable ans to a matrix of size n*n with all elements as 0.
# 2. Initialize a variable mat to a matrix of size n*n with all elements as tuples of the form (i,j) where i and j are the row and column indices respectively.
# 3. Define a spiralOrder function which takes a matrix as parameter and returns the elements of the matrix in spiral order as a list by popping the first row and calling the spiralOrder function on the transpose of the matrix.
# 4. Call the spiralOrder function with mat as parameter and store the result in a variable order.
# 5. For each index ind and value v in order, set the element at the indices v[0] and v[1] in ans to ind+1.
# 6. Return ans.