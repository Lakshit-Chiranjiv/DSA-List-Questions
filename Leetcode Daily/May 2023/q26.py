class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def solve(m,i,ch):
            if i >= len(piles):
                return 0
            ans = 0 if ch==0 else float('inf')
            tot = 0
            for X in range(1,2*m+1):
                if i + X > len(piles):
                    break
                tot += piles[i+X-1]

                if ch == 0:
                    ans = max(ans,tot+solve(max(m,X),i+X,1))
                else:
                    ans = min(ans,solve(max(m,X),i+X,0))
            return ans

        return solve(1,0,0)

# intuition:
# 1. We can simulate a game here and in alice's turn we will try to maximize the score and in bob's turn we will try to minimize the score.
# 2. Carry 3 parameters: the number of piles allowed to take, the current index and the current player.
# 3. Return the maximum score alice can get.

# solution:
# 1. Create a recursive function solve(m,i,ch) where m is the number of piles allowed to take, i is the current index and ch is the current player.
# 2. If the current index is greater than or equal to the length of the piles, return 0. (base case)
# 3. Initialize ans = 0 if ch == 0 which means it is alice's turn else initialize ans = inf which means it is bob's turn.
# 4. Initialize tot = 0 which will store the sum of the piles till each index.
# 5. Iterate over piles from 1 to 2*m+1 and if the current index + X is greater than the length of the piles, break.
# 6. Add the current pile to tot.
# 7. If ch == 0, it is alice's turn so update ans = max(ans,tot+solve(max(m,X),i+X,1)) else it is bob's turn so update ans = min(ans,solve(max(m,X),i+X,0)).
# 8. Return ans.
# 9. Return solve(1,0,0) which means initially alice can take 1*2 pile, the current index is 0 and it is alice's turn.