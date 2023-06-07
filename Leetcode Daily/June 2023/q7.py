class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        def pad(x,l):
            x = ("0"*(l-len(x)))+x
            return x
        a = str(bin(a))[2:]
        b = str(bin(b))[2:]
        c = str(bin(c))[2:]
        l = max(len(a),len(b),len(c))
        a = pad(a,l)
        b = pad(b,l)
        c = pad(c,l)

        i = l-1
        ans = 0
        while i >= 0:
            if c[i] == '0':
                if a[i] == '1':
                    ans += 1
                if b[i] == '1':
                    ans += 1
            else:
                if a[i] == '0' and b[i] == '0':
                    ans += 1
            i -= 1
        return ans
    
# intuition:
# 1. If we need bit to be 0, then we need to flip both a and b if they are 1.
# 2. If we need bit to be 1, then we need to flip either a or b if they are 0.
# 3. These are the only two cases we need to consider for minimum flips.

# solution:
# 1. Define a function to pad the binary strings with 0s to make them of equal length.
# 2. Convert a, b and c to binary strings using bin() function.
# 3. Pad a, b and c to make them of equal length using the function defined in step 1.
# 4. Iterate over the strings from right to left and check the following:
# 5. If c[i] == '0', then check if a[i] == '1' and b[i] == '1'. If yes, then we need to flip both a and b. So, increment ans by 1 for each flip i.e. increment ans by 2.
# 6. If c[i] == '1', then check if a[i] == '0' and b[i] == '0'. If yes, then we need to flip either a or b. So, increment ans just by 1.
# 7. Return ans.

# Time Complexity: O(log(max(a,b,c))) as we are iterating over the binary strings of a, b and c.
# Space Complexity: O(log(max(a,b,c))) as we are storing the binary strings of a, b and c.