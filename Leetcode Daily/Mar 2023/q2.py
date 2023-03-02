class Solution:
    def compress(self, chars: List[str]) -> str:
        s = ""
        c = 0
        if len(chars) == 1:
            return 1
        for i in range(len(chars)-1):
            c += 1
            if chars[i] != chars[i+1]:
                if c == 1:
                    s += chars[i]
                else:
                    s += (chars[i]+str(c))
                c = 0
            
        if chars[len(chars)-1] == chars[len(chars)-2]:
            s += (chars[len(chars)-1]+str(c+1))
        else:
            s += chars[len(chars)-1]

        m = list(s)
        chars[:len(s)] = m

        return len(s)