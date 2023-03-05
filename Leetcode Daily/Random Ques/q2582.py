class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        ftb = True
        x = n-1
        while time > x:
            time -= x
            ftb = not ftb
            
        if ftb:
            return 1 + time
        else:
            return n - time