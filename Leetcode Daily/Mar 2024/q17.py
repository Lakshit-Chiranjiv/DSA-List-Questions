class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        # Case 1: No overlapping before merging intervals
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Case 2: Overlapping and merging intervals
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # Case 3: No overlapping after merging newInterval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
    
# 57. Insert Interval
# Time Complexity: O(n)
# Space Complexity: O(n)
    
# We iterate through the intervals and keep adding the non-overlapping intervals to the result. We merge the overlapping intervals with the newInterval and keep updating the newInterval. We add the newInterval to the result after merging all the overlapping intervals. We add the remaining non-overlapping intervals to the result. We return the result at the end.