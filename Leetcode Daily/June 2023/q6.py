class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)-2):
            if arr[i+1]-arr[i] != arr[i+2]-arr[i+1]:
                return False
        return True

# intuition:
# 1. Sorting the array in any order will bring the elements in order. And an AP is always sorted.
# 2. So, we sort the array and check if the difference between any two adjacent elements is the same for all the elements.
# 3. If the difference between any two adjacent elements is not the same, then the array is not an AP. So, we return False.

# solution:
# 1. We sort the array using the sort() function.
# 2. We iterate over the array using a for loop considering 3 elements at a time using the range of the for loop as range(len(arr)-2).
# 3. We check if the difference between any two adjacent elements is the same. If not, then we return False.
# 4. If the difference between any two adjacent elements is the same, then we return True at the end of the for loop.

# Time Complexity: O(nlogn)
# Space Complexity: O(1)