class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            bricks -= diff
            heapq.heappush(heap, -diff)

            if bricks < 0:
                if ladders == 0:
                    return i
                bricks += -heapq.heappop(heap)
                ladders -= 1
        return len(heights)-1

# 1642. Furthest Building You Can Reach
# Time complexity: O(nlogk)
# Space complexity: O(n)

# We use a max heap to store the differences between the heights of the buildings. We then iterate through the list and keep track of the differences between the heights of the buildings. We then use the bricks to cover the differences and if we run out of bricks, we use the ladders to cover the differences, the differences which are maximum. We then return the index of the last building we can reach.