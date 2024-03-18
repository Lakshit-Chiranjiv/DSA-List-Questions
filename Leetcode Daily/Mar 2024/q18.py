class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = len(points)
        points.sort()
        prev = points[0]

        for i in range(1, len(points)):
            curr = points[i]

            if curr[0] <= prev[1]:
                ans -= 1
                prev = [curr[0], min(curr[1], prev[1])]
            else:
                prev = curr
        return ans
    
# 452. Minimum Number of Arrows to Burst Balloons
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
    
# We sort the points based on the start of the intervals. We iterate through the points and keep track of the previous interval. If the current interval overlaps with the previous interval, we decrement the answer and update the previous interval to the overlapping interval. If the current interval does not overlap with the previous interval, we update the previous interval to the current interval. We return the answer at the end.