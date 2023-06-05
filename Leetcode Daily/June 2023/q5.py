class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(len(coordinates)-2):
            ax,ay = coordinates[i][0],coordinates[i][1]
            bx,by = coordinates[i+1][0],coordinates[i+1][1]
            cx,cy = coordinates[i+2][0],coordinates[i+2][1]
            if ((cx-bx) == 0 or (bx-ax) == 0):
                if (cx-bx) != (bx-ax):
                    return False
                else:
                    continue
            if ((cy-by)/(cx-bx)) != ((by-ay)/(bx-ax)):
                return False
        return True
    
# intution:
# 1. The slope of any two points in a straight line is the same. For all points to be in a straight line, the slope of any two points should be the same.
# 2. So, we can move on considering 3 points at a time and check if the slope of all the adjacent points is the same.
# 3. If the slope of any two points is different, then the points are not in a straight line. So, we return False.

# solution:
# 1. We iterate over the given points using a for loop and consider 3 points at a time by using the range of the for loop as range(len(coordinates)-2).
# 2. We store the coordinates of the 3 points in ax,ay,bx,by,cx,cy.
# 3. Perform the base case check for any denominator being 0 while calculating the slope. If any of the denominators is 0, then we check if the other denominator is also 0. If not, then we return False. Else, we continue with the next iteration.
# 4. If the slope of any two points is different, then we return False. Slope is calculated as (y2 - y1)/(x2 - x1).
# 5. If all the slopes are the same, then we return True at the end of the for loop.

# Time Complexity: O(n)
# Space Complexity: O(1)