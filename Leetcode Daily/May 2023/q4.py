class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        n = len(senate)
        r,d = deque(), deque()

        for i,c in enumerate(senate):
            if c == 'R':
                r.append(i)
            else:
                d.append(i)

        while r and d:
            dval = d.popleft()
            rval = r.popleft()

            if rval < dval:
                r.append(rval+n)
            else:
                d.append(dval+n)
            
        return "Radiant" if r else "Dire"


# intuition:
# 1. One thing is sure that we have to go from left to right. 
# 2. To play optimally, each player will ban the next closest opponent.
# 3. Another thing is that we can go circularly. So, after one iteration, again the last player can ban the first opponent.
# 4. Keeping this in mind, we can use two queues to store the indices of the players. One queue for the Radiant players and the other for the Dire players.
# 5. We can iterate over the senate string and add the indices of the players to the respective queues. Then perform ban operations on the players optimally.
# 6. In the end, whichever queue is not empty will be the winner.

# solution:
# 1. Initialize two queues, one for the Radiant players and the other for the Dire players.
# 2. Iterate over the senate string. If the current character is R, add the index to the Radiant queue. If the current character is D, add the index to the Dire queue.
# 3. While both the queues are not empty, pop the first element from both the queues. If the index of the Radiant player is less than the index of the Dire player, add the index of the Radiant player to the Radiant queue by adding n to it. Else, add the index of the Dire player to the Dire queue by adding n to it.
# 4. Return the winner by checking which queue is not empty.

# Time Complexity: O(n) where n is the length of the senate string. We iterate over the senate string once and perform ban operations on the players optimally.

# Space Complexity: O(n) where n is the length of the senate string. We use two queues to store the indices of the players. In the worst case, all the players can be of the same type. In that case, we will have to store all the indices in the respective queues.