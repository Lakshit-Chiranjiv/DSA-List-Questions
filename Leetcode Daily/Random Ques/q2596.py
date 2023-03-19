class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        s = 0
        n = len(grid)
        i = 0
        j = 0
        lm = (n*n)-1
        def validMove(i,j):
            return (i >= 0 and i < n and j >= 0 and j < n)
        
        while s < lm:
            vdl = [i+2,j-1]
            vdr = [i+2,j+1]
            vul = [i-2,j-1]
            vur = [i-2,j+1]
            hlu = [i-1,j-2]
            hru = [i-1,j+2]
            hld = [i+1,j-2]
            hrd = [i+1,j+2]
            moves = [vdl,vdr,vul,vur,hlu,hru,hld,hrd]
            flag = 0
            for move in moves:
                x = move[0]
                y = move[1]
                if validMove(x,y):
                    if grid[x][y] == s+1:
                        s += 1
                        i = x
                        j = y
                        flag = 1
                        break
            if flag == 0: return False
        return True