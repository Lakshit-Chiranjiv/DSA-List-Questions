class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            a = stones[-1]
            b = stones[-2]
            stones.pop()
            stones.pop()
            if a!=b:
                stones.append(max(a,b)-min(a,b))
        
        if len(stones) == 0:
            return 0
        return stones[0]

# intuition:
# 1. We will keep sorting and extracting the last 2 elements as per the given constraints until there is only 1 element left.
# 2. If the last 2 elements are equal, we will remove them from the list else we will add the difference of the 2 elements to the list.
# 3. If the list is empty, we will return 0 else we will return the last element of the list.

# solution:
# 1. Create a while loop that will run until there is only 1 element left in the list.
# 2. Sort the list.
# 3. Extract the last 2 elements of the list.
# 4. Remove the last 2 elements from the list.
# 5. If the last 2 elements are not equal, we will add the difference of the 2 elements to the list.
# 6. After the while loop, if the list is empty, we will return 0 else we will return the last element of the list.



# Time complexity: O(nlogn) where n is the length of the list as we need to sort the list and extract the last 2 elements.
# Space complexity: O(1) as we are not using any extra space.