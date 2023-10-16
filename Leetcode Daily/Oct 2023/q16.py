class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            next = [0]*(len(res)+1)
            for j in range(len(res)):
                next[j] += res[j]
                next[j+1] += res[j]

            res = next
        return res