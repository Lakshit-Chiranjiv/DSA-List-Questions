class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        sm = 0
        sm += min(k,numOnes)
        k -= min(k,numOnes)
        if k > 0:
            k -= min(k,numZeros)
            if k > 0:
                sm -= min(k,numNegOnes)
                k -= min(k,numNegOnes)
                
        return sm