class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mp = {}
        for i in arr:
            if mp.get(i,0) == 0:
                mp[i] = 1
            else:
                mp[i] += 1
        dc = dict(sorted(mp.items(), key=lambda item: item[1]))
        n = len(dc)
        c = 0
        for i in dc:
            if k >= dc[i]:
                c += 1
                k -= dc[i]
            if k <= 0:
                break
        return n-c

# 1481. Least Number of Unique Integers after K Removals
    
# Time complexity: O(nlogn)
# Space complexity: O(n)
    
# We create a dictionary to store the frequency of each element in the list. We then sort the dictionary based on the frequency of the elements. We then iterate through the dictionary and keep track of the number of unique elements we have removed. We keep removing the elements till we have removed k elements and then return the number of unique elements left.