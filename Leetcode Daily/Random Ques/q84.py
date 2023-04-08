class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        mxa = 0
        n = len(heights)

        for i in range(n+1):
            while st and (i == n or heights[st[-1]] >= heights[i]):
                ht = heights[st[-1]]
                st.pop()
                wd = 0
                if len(st)==0: wd = i
                else:
                    wd = i - st[-1] - 1
                mxa = max(mxa,wd*ht)
            st.append(i)
        return mxa
