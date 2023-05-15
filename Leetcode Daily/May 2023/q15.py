class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fval = head
        bval = head
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        
        for i in range(k-1):
            fval = fval.next

        k = n-k+1

        for i in range(k-1):
            bval = bval.next
        
        fval.val, bval.val = bval.val, fval.val
        return head
    
# intution:
# 1. We simply make two iterations for the kth node from the front and the kth node from the back by using two variables to store the nodes.
# 2. Then we simply swap the values of the two nodes and return the head.

# solution
# 1. Initialize two variables fval and bval to head.
# 2. Initialize a variable n to 0 for storing the length of the linked list and a variable curr to head.
# 3. Iterate over the linked list and increment n and curr.
# 4. Then we iterate over the linked list again for k-1 times and update fval to fval.next. This will give us the kth node from the front.
# 5. Then we update k to n-k+1 and iterate over the linked list again for k-1 times and update bval to bval.next. This will give us the kth node from the back.
# 6. Then we simply swap the values of the two nodes and return the head.

# Time Complexity: O(n) where n is the length of the linked list as we make two iterations over the linked list. One for calculating the length and the other for finding the kth node from the front and the back.

# Space Complexity: O(1) as we do not use any extra space.