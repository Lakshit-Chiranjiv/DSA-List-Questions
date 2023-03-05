class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        ans = ""
        idx = 0
        for i in s:
            if i == '6':
                ans += '9'
                break
            else:
                ans += i
            idx += 1
        ans = ans + s[idx+1:]
        return int(ans)