class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        st = set()
        a = 0
        b = 0
        for i in A:
            if i in st:
                a = i
            else:
                st.add(i)
        for i in range(1,len(A)+1):
            if i not in st:
                b = i
                break
        return [a,b]