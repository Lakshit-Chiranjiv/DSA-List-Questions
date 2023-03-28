class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        mp = {}
        for i in days:
            mp[i] = 1

        dp = [0 for i in range(366)]

        for i in range(1,366):
            if mp.get(i,0) == 0:
                dp[i] = dp[i-1]

            else:
                dp[i] = min(dp[i-1]+costs[0], dp[i-7]+costs[1], dp[i-30]+costs[2])

        return dp[365]
    
# intution
# 1. Minimum cost to travel on all given days is required.
# 2. We can travel on any day, but we have to pay for the ticket for that day.
# 3. We can buy a 1-day, 7-day or 30-day ticket. Then we can travel on any day within that period and select the ticket that is cheapest.
# 4. We can use dynamic programming to solve this problem.
# 5. We can use a dp array to store the minimum cost to travel on each day.
# 6. A hashmap is used to store the days on which we have to travel.
# 7. Depending on the day, we can either buy a ticket or not buy a ticket.


# solution:
# 1. Initialize a hashmap to store the days on which we have to travel.
# 2. Initialize a dp array to store the minimum cost to travel on each day.
# 3. Iterate over the days array and store the days on which we have to travel in the hashmap.
# 4. Iterate over the dp array from index 1 to 365.
# 5. If the day is not in the hashmap, then we can travel on that day without buying a ticket. So, the minimum cost to travel on that day is the same as the minimum cost to travel on the previous day.
# 6. If the day is in the hashmap, then we have to buy a ticket. So, we can buy a 1-day, 7-day or 30-day ticket. Then we can travel on any day within that period and select the ticket that is cheapest.
# 7. For a 1-day ticket, the minimum cost to travel on that day is the minimum cost to travel on the previous day plus the cost of the 1-day ticket.
# 8. For a 7-day ticket, the minimum cost to travel on that day is the minimum cost to travel on the day 7 days before that day plus the cost of the 7-day ticket.
# 9. For a 30-day ticket, the minimum cost to travel on that day is the minimum cost to travel on the day 30 days before that day plus the cost of the 30-day ticket.
# 10. Return the minimum cost to travel on the last day.

# time complexity: O(n) where n is the number of days. We iterate over the dp array once. Accessing the hashmap is O(1) on average.
# space complexity: O(n) where n is the number of days. We use a hashmap and a dp array of size 366.