class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in s:
            if i == '*' and len(st)>0:
                st.pop()
            else:
                st.append(i)

        ans = ''.join(st)
        return ans
    
# intuition:
# 1. As we need to remove the last occurring non-star character when we encounter a star, a stack is suitable for this problem.
# 2. Keep pushing the non-star characters into the stack.
# 3. If we encounter a star, we pop the last element from the stack.
# 4. Join the stack from bottom to top and return the string.

# solution:
# 1. Create a stack.
# 2. Iterate through the string.
# 3. If the current character is a star, we pop the last element from the stack.
# 4. If the current character is a non-star character, we push it into the stack.
# 5. Join the stack from bottom to top and return the string.

# time complexity: O(n) where n is the length of the string. We iterate through the string once.
# space complexity: O(n) where n is the length of the string. We use a stack to keep track of the non-star characters.