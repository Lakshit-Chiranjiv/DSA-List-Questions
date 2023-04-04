class Solution:
    def partitionString(self, s: str) -> int:
        mp = {}
        ans = 1
        for i in s:
            if mp.get(i,0) == 0:
                mp[i] = 1
            else:
                ans += 1
                for j in mp:
                    mp[j] = 0
                mp[i] = 1
        
        return ans
    
# intution:
# 1. As we don't need repeated characters in a partition, we will obviously need something to keep track of the frequency of each character.
# 2. We will use a hashmap for that.
# 3. We will traverse the string and keep adding the characters to the hashmap if they are not present.
# 4. If the character is already present, we will increment the count of the partitions and reset the hashmap to 0.
# 5. We will return the count of the partitions at the end.

# solution:
# 1. Create a hashmap to keep track of the frequency of each character.
# 2. Initialize the ans variable to 1 as we will have atleast 1 substring.
# 3. Traverse the string and check if the character is present in the hashmap or not.
# 4. If it is not present, we will add it to the hashmap and put the value as 1.
# 5. If it is present, we will increment the count of the partitions and reset all the values in the hashmap to 0. Add the current character to the hashmap and put the value as 1.
# 6. Return the ans variable at the end.

# Time complexity: O(n) as we are traversing the string only once. In the loop, we also traversed the map which in the worst case can have 26 characters. So, the time complexity in worst case can be considered as O(26*n) which is O(n).

# Space complexity: O(1) as we are using a hashmap where at max we can have 26 characters. So, the space complexity is O(1).