def numberOfSteps(self, num: int) -> int:
    c = 0
    while num != 0:
        if num & 1 == 1:
            num -= 1
        else:
            num //= 2
        c += 1
    return c