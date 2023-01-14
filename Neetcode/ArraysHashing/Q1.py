# contains duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        st = set()
        for i in nums:
            if i in st:
                return True
            else:
                st.add(i)
        return False