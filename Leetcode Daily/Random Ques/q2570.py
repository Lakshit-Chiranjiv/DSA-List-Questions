class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        mp = {}
        for i in nums1:
            if mp.get(i[0],0) == 0:
                mp[i[0]] = i[1]
            else:
                mp[i] += 1
                
        for i in nums2:
            if mp.get(i[0],0) == 0:
                mp[i[0]] = i[1]
            else:
                mp[i[0]] += i[1]
                
        ans = []
        for i in mp:
            ans.append([i,mp[i]])
            
        ans.sort()
        return ans