def sortArrayByParity(self, nums: List[int]) -> List[int]:
    ev = []
    od = []
    for i in nums:
        if i & 1 == 1:
            od.append(i)
        else:
            ev.append(i)

    ans = ev+od
    return ans