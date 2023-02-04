def convert(self, s: str, numRows: int) -> str:
    n = len(s)
    if numRows == 1:
        return s
    arr = [['' for i in range(n)] for j in range(numRows)]
    i = 0
    j = 0
    k = 0
    while k < n:
        while i < numRows and k < n:
            arr[i][j] = s[k]
            i += 1
            k += 1
        i -= 2
        j += 1
        while i >= 0 and k < n:
            arr[i][j] = s[k]
            i -= 1
            j += 1
            k += 1
        i += 2
        j -= 1
    
    ans = ''
    for i in range(numRows):
        for j in range(n):
            if arr[i][j] != '':
                ans += arr[i][j]
    return ans  