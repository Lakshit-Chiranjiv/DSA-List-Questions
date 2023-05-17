class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        n = len(arr)
        i = 0 
        j = n-1
        sm = 0
        while i < j:
            sm = max(sm,arr[i]+arr[j])
            i += 1
            j -= 1

        return sm

# intuition:
# 1. Simply store the values in an array and take two pointers at start and end of the array.
# 2. Keep updating the sum and return the maximum sum.

# solution:
# 1. Create an empty list.
# 2. Traverse the linked list and store the values in the list.
# 3. Take two pointers i and j at start and end of the list.
# 4. Take a sum variable and initialize it to 0.
# 5. Traverse the list till i < j and keep updating the sum by the maximum of sum and arr[i]+arr[j].
# 6. Return the maximum sum.

# Time Complexity: O(n) where n is the number of nodes in the linked list and we traverse the linked list once to store the values in the list and once to find the maximum sum.

# Space Complexity: O(n) where n is the number of nodes in the linked list and we store the values in the list.