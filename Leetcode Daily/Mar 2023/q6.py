class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        c = 0
        x = 0
        for i in range(1,arr[len(arr)-1]+k+1):
            if c >= len(arr) or i != arr[c]:
                x += 1
                if x == k:
                    return i
            else:
                c += 1
        return -1