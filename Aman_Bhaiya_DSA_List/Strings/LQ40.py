class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lst = list(s)
        new_lst = filter(lambda x: ((x >= 'a' and x<='z') or (x>='0' and x<='9')), lst)
        new_lst = list(new_lst)
        s = ''.join(new_lst)
        t = ''.join(new_lst[::-1])
        return s==t