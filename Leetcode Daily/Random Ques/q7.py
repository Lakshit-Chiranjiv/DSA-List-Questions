class Solution:
    def reverse(self, x: int) -> int:
        a = -2 ** 31
        b = 2**31 - 1
        if x < 0:
            x = int("-"+str(x)[::-1][:-1])
        else:
            x = int(str(x)[::-1])
        return 0 if (x<a or x>b) else x