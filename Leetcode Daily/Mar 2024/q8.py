class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mp = {}
        for i in nums:
            if mp.get(i,0) == 0:
                mp[i] = 1
            else:
                mp[i] += 1
        mx, ans = 0, 0
        for i in mp:
            mx = max(mx,mp[i])
        for i in mp:
            ans += (mp[i] if mp[i] == mx else 0)
        return ans
    
# 3005. Count Elements With Maximum Frequency
# Time Complexity: O(n)
# Space Complexity: O(n)
    
# We maintain a dictionary to store the frequency of each element. We then find the maximum frequency and count the number of elements with that frequency. We return the count.