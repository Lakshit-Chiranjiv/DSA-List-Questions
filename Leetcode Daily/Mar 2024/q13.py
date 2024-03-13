class Solution:
    def pivotInteger(self, n: int) -> int:
        s = (n*(n+1))//2
        for i in range(1,n+1):
            if (s+i) % 2 == 0 and (s - ((i*(i-1))//2)) == ((i*(i+1))//2):
                return i
        return -1

# 2485. Find the Pivot Integer
# Time Complexity: O(n)
# Space Complexity: O(1)

# As we see that if the pivot exists, then it will be added on both the sides to check for equality. So, we calculate the sum of the first n natural numbers and then iterate through the numbers from 1 to n and check if the sum of the first i natural numbers and the sum of the remaining natural numbers are equal including the pivot on both sides. If we find such a number, we return it. If we don't find such a number, we return -1.