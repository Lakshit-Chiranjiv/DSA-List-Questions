import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for i in nums:
            if mp.get(i,0) == 0:
                mp[i] = 1
            else:
                mp[i] += 1

        keys = list(mp.keys())
        values = list(mp.values())
        sorted_value_index = np.argsort(values)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

        keys = list(sorted_dict.keys())

        ans = []
        keys.reverse()
        for i in range(k):
            ans.append(keys[i])

        return ans

# intuition:
# 1. Keep a frequency map of all the elements in the array.
# 2. Sort the frequency map in ascending order.
# 3. Return the last k elements of the sorted frequency map.

# solution:
# 1. Create a frequency map of all the elements in the array by iterating over the array once.
# 2. Extract the keys and values of the frequency map and store them in two separate arrays.
# 3. Sort the values array in ascending order and store the sorted indices in a separate array using argsort() function.
# 4. Create a new dictionary and store the keys and values in the sorted order of the values array using the sorted indices array.
# 5. Extract the keys from the sorted dictionary and store them in a separate array.
# 6. Reverse the keys array and return the first k elements of the array.

# Time Complexity: O(nlogn) where n is the number of elements in the array. The time complexity is dominated by the sorting step. The rest of the steps take O(n) time.

# Space Complexity: O(n) where n is the number of elements in the array. The frequency map will contain n entries at most. The sorted indices array will contain n entries. The sorted dictionary will contain n entries. The keys array will contain n entries.