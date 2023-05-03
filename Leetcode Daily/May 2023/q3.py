class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1).difference(nums2)), list(set(nums2).difference(nums1))]
    
# intuition:
# 1. First method can be to create a hash map and store value 1 against each element of nums1 to indicate that the element is present in nums1.
# 2. Then, we can iterate over nums2 and check if the element is present in the hash map. If it is, we can change it value to 3 to indicate that the element is present in both the arrays. If it is not, we can add it to the hash map with value 2 to indicate that the element is present in nums2.
# 3. After the loop completes, we can iterate over the hash map and add the elements with value 2 to the answer array. These elements are present in nums2 but not in nums1. We can also add the elements with value 1 to the answer array. These elements are present in nums1 but not in nums2.
# 4. Return the answer array.
# 5. Another method can be to convert to set and find the difference between the two sets. The difference between the two sets will give us the elements that are present in one set but not in the other.

# solution:
# 1. Initialize a hash map.
# 2. Iterate over nums1. Add each element to the hash map with value 1.
# 3. Iterate over nums2. If the current element is present in the hash map, change its value to 3. If it is not, add it to the hash map with value 2.
# 4. Initialize two empty arrays, one for the elements present in nums1 but not in nums2 and the other for the elements present in nums2 but not in nums1.
# 5. Iterate over the hash map. If the value of the current element is 2, add it to the second array. If the value of the current element is 1, add it to the first array.
# 6. Return the two arrays.
# 7. For the second method, convert nums1 and nums2 to sets. Find the difference between the two sets. The difference between the two sets will give us the elements that are present in one set but not in the other. Put these elements in two arrays and return them.

# Time Complexity: O(n) where n is the length of the longer array. We iterate over both the arrays once. In case of the second method, we convert the arrays to sets. This takes O(n) time as well.

# Space Complexity: O(n) where n is the length of the longer array. We use a hash map to store the elements of the longer array. In case of the second method, we convert the arrays to sets. This takes O(n) space as well.