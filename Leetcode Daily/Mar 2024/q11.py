class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mp = {}
        for i in s:
            if mp.get(i,0) == 0:
                mp[i] = 1
            else:
                mp[i] += 1
        mpo = {}
        for i in order:
            if mpo.get(i,0) == 0:
                mpo[i] = 1
        ans = ""
        tmp = ""
        for i in order:
            if mp.get(i,0) > 0:
                ans += (mp[i]*i)
        for i in s:
            if mpo.get(i,0) == 0:
                tmp += (mp[i]*i)
                mpo[i] = 1
        return ans+tmp
    
# 791. Custom Sort String
# Time Complexity: O(n)
# Space Complexity: O(n)

# We first create a dictionary to store the frequency of each character in the string s. We then create another dictionary to store the existence of each character in the order string by just storing 1 as value against the character if it exists in order. We then iterate through the order string and add the characters to the answer string according to their frequency in the string s. This ensures that the characters are added in the order specified by the order string. We then iterate through the string s and add the characters to the tmp string which are not present in the order string. We then add the tmp string to the answer string and return the answer string.