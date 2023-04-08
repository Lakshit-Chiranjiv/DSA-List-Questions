class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights):
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
        if len(matrix)==0: return 0
        m = len(matrix)
        n = len(matrix[0])
        heights = [0]*n
        mxa = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1': heights[j] += 1
                else: heights[j] = 0
            mxa = max(mxa,largestRectangleArea(heights))
        return mxa