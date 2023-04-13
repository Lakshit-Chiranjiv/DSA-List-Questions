class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popc = 0
        st = []
        for i in pushed:
            st.append(i)
            while st and st[-1]==popped[popc]:
                st.pop()
                popc += 1
        
        return len(st) == 0
    

#intuition:
# 1. If all the elements follow a stack push and pop order then the stack will be empty at the end.
# 2. So, we can have a pointer to the popped array and iterate over the pushed array.
# 3. If the top element of the stack is equal to the element pointed by the popped pointer then pop the element and increment the popped pointer.
# 4. If the stack is empty at the end then return True else return False.

# solution:
# 1. Create a stack and a pointer to the popped array.
# 2. Iterate over the pushed array.
# 3. Push the element into the stack.
# 4. While the stack is not empty and the top element of the stack is equal to the element pointed by the popped pointer then pop the element and increment the popped pointer.
# 5. If the stack is empty at the end then return True else return False.

# Time complexity: O(n) where n is the length of the pushed array as we are iterating over the pushed array once.
# Space complexity: O(n) where n is the length of the pushed array as we are using a stack to store the pushed elements.