class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.count = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]
        self.count -= 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))

        fact_index = {}
        for i, n in enumerate(nums):
            f = 2
            while f*f <= n:
                if n % f == 0:
                    if f in fact_index:
                        uf.union(i, fact_index[f])
                    else:
                        fact_index[f] = i
                    while n % f == 0:
                        n = n // f
                f += 1
            if n > 1:
                if n in fact_index:
                    uf.union(i, fact_index[n])
                else:
                    fact_index[n] = i
        return uf.count == 1

# 2709. Greatest Common Divisor Traversal
# Time complexity: O(N*sqrt(N))
# Space complexity: O(N)
    
# The idea is to use union find to connect all the numbers that have the same prime factors. For each number, we find its prime factors and connect it with the previous number that has the same prime factors. If we can connect all the numbers, then we can traverse all the pairs. Otherwise, we cannot. The time complexity is O(N*sqrt(N)) because we need to find the prime factors of each number. The space complexity is O(N) because we need to store the prime factors of each number. If at last we have a single connected component, then we can traverse all the pairs. Otherwise, we cannot.