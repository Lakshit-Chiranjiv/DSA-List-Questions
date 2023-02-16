class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        a = int(''.join(list(map(lambda x: str(x), num))))
        s = str(a+k)
        ans = list(map(lambda x: int(x),list(s)))
        return ans