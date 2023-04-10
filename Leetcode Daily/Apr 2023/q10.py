class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if i == ')':
                    if len(stack) == 0 or stack.pop() != '(':
                        return False
                if i == '}':
                    if len(stack) == 0 or stack.pop() != '{':
                        return False
                if i == ']':
                    if len(stack) == 0 or stack.pop() != '[':
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
        
# intuition:
# 1. A stack is suitable for such problems where we need to keep track of the last element.
# 2. Keep pushing the opening brackets into the stack.
# 3. If we encounter a closing bracket, we check if the last element in the stack is the corresponding opening bracket. If it is, we pop the last element from the stack. If it is not, we return False.
# 4. If the stack is empty at the end, we return True. Else, we return False.

# solution:
# 1. Create a stack.
# 2. Iterate through the string.
# 3. If the current character is an opening bracket, we push it into the stack.
# 4. If the current character is a closing bracket, we check if the last element in the stack is a corresponding opening bracket. If it is, we pop the last element from the stack. If it is not or if the stack is empty, we return False.
# 5. If the stack is empty at the end, we return True. Else, we return False.

# time complexity: O(n) where n is the length of the string. We iterate through the string once.
# space complexity: O(n) where n is the length of the string. We use a stack to keep track of the opening brackets.