class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        xdif = abs(sx-fx)
        ydif = abs(sy-fy)
        if xdif == 0 and ydif == 0 and t == 1:
            return False
        return (min(xdif,ydif) + abs(xdif-ydif)) <= t
            