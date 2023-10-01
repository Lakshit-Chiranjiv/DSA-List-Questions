class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split(' ')
        y = []
        for i in x:
            y.append(''.join(reversed(list(i))))
        return ' '.join(y)