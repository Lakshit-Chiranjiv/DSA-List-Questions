class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1,n2) for n1,n2 in zip(nums1,nums2)]
        pairs.sort(key=lambda x: x[1], reverse=True)

        minHeap = []
        sm = 0
        ans = 0

        for n1,n2 in pairs:
            sm += n1
            heapq.heappush(minHeap, n1)
            if len(minHeap) > k:
                n1Pop = heapq.heappop(minHeap)
                sm -= n1Pop
            if len(minHeap) == k:
                ans = max(ans, sm*n2)
            
        return ans
    
# intuition:
# 1. Here DP won't work because the constraints are too high and we won't get too many overlapping subproblems.
# 2. A greedy approach with respect to the first array would be sufficient if we sort the second array in descending order.
# 3. We need to maximize the sum of the first array and the product of the second array. So first of all we will sort the 2nd array in descending order and keep checking what is the maximum sum possible if we take the current element of the 2nd array as minimum.
# 4. For keeping only k elements, we will use a min heap so that whenever the size of the heap becomes greater than k, we will pop the minimum element from the heap.
# 5. We will keep a running sum of the elements in the heap and multiply it with the current element of the 2nd array and update the answer.

# solution:
# 1. Create an array of pairs of nums1 and nums2 and sort it in descending order of nums2.
# 2. Create a min heap and a variable sm to keep track of the sum of the elements in the heap. Also create a variable ans to keep track of the answer.
# 3. Iterate over the array of pairs and add the current element of nums1 to sm and push it to the heap. If the size of the heap becomes greater than k, pop the minimum element from the heap and subtract it from sm.
# 4. If the size of the heap becomes equal to k, update the answer by multiplying sm with the current element of nums2.
# 5. Return the answer.

# Time Complexity: O(nlogn)

# Space Complexity: O(n)