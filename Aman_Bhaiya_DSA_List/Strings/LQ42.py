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