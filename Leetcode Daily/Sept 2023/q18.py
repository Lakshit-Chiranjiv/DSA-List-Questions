class Solution:
    def kWeakestRows(self, mat, k):
        rows = len(mat)
        cols = len(mat[0])

        arr = [0] * rows
        for i in range(rows):
            count1 = 0
            for j in range(cols):
                if mat[i][j] == 1:
                    count1 += 1
                else:
                    break
            arr[i] = count1

        ans = [0] * k
        for i in range(k):
            min_val = float('inf')
            min_index = 0
            for j in range(len(arr)):
                if arr[j] < min_val:
                    min_val = arr[j]
                    min_index = j
            ans[i] = min_index
            arr[min_index] = float('inf')

        return ans