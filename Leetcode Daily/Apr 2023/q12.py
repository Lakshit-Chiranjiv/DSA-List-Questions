class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        arr = path.split('/')
        def filterpaths(x):
            return x!='.' and x!=''
        filt_arr = list(filter(filterpaths,arr))
        for i in filt_arr:
            if i != '..':
                st.append(i)
            else:
                if len(st)>0:
                    st.pop()

        print(filt_arr)
        print(st)
        ans = ''
        for i in st:
            ans = ans + '/' + i

        if not ans:
            return '/'          
        return ans
    
# intution:
# 1. As we know a folder can be represented by a stack, so we can use a stack to solve this problem.
# 2. We can split the path by '/' and then filter out the empty strings and '.' to get the actual folders.
# 3. Now simply put the folders in the stack and if we encounter a '..' then pop the top element of the stack.
# 4. Finally, we can join the stack elements to get the simplified path.

# solution:
# 1. Create a stack.
# 2. Split the path by '/'.
# 3. Filter out the empty strings and '.' using filter function and store the result in a list.
# 4. Iterate over the list and if the element is not '..' then push it into the stack.
# 5. If the element is '..' then pop the top element of the stack.
# 6. Finally, join the stack elements with '/' and return the result.
# 7. If the stack is empty then return '/'. 
# 
# Time complexity: O(n) where n is the length of the path as we are iterating over the path once.
# Space complexity: O(n) where n is the length of the path as we are using a stack to store the folders. 