class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        if len(s1) != len(s2) or sorted(s1) != sorted(s2) or len(s1)==1: return False

        @cache
        def solve(s1,s2):
          n = len(s1)
          if s1 == s2: return True
          if n != len(s2) or sorted(s1) != sorted(s2) or n==1: return False

          for i in range(1,n):
            notSwap = solve(s1[:i],s2[:i]) and solve(s1[i:],s2[i:])
            swap = solve(s1[:i],s2[n-i:]) and solve(s1[i:],s2[:n-i])

            if notSwap or swap: return True

          return False
            
        return solve(s1,s2)

# intution:
# 1. It is one of the partition DP problem.
# 2. We can partition the string into two parts at every index.
# 3. Then there are two choices - either swap the two parts or not.
# 4. Swap case will check the left part of s1 with right part of s2 and vice versa.
# 5. Not swap case will check the left part of s1 with left part of s2 and vice versa.
# 6. If any of the two cases is true, then we return true.
# 7. Else we return false.
# 8. There are also some base cases - if the strings are equal return true, if the length of the strings are not equal return false, if the length of the string is 1 and the strings are not equal return false.
# 9. We can memoize the function to reduce the time complexity.

# solution:
# 1. Check if the strings are equal, if they are return true.
# 2. Check if the length of the strings are not equal or if the sorted strings are not equal or if the length of the string is 1, if any of these are true return false.
# 3. Create a function solve which takes two strings as parameters.
# 4. Check if the strings are equal withing the function, if they are return true.
# 5. Check if the length of the strings are not equal or if the sorted strings are not equal or if the length of the string is 1, if any of these are true return false.
# 6. Create a for loop which iterates from 1 to the length of the string.
# 7. Create a notSwap variable which stores the result of calling the solve function with the left part of s1 and left part of s2 and the right part of s1 and right part of s2.
# 8. Create a swap variable which stores the result of calling the solve function with the left part of s1 and right part of s2 and the right part of s1 and left part of s2.
# 9. Check if either of the two variables is true, if they are return true.
# 10. Else return false outside the for loop.
# 11. Return the result of calling the solve function with s1 and s2.
# 12. Create a cache decorator to memoize the function.




