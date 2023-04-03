class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        boats = 0
        while i <= j:
            if people[j] + people[i] <= limit:
                i += 1
            j -= 1
            boats += 1
        return boats

# intution: 
# 1. Only 2 people can fit in a boat at a time.
# 2. So to best utilize the limit, we should pair the heaviest person with the lightest person.
# 3. If the sum of the heaviest and lightest person is greater than the limit, then the heaviest person cannot pair with anyone. So, we can send him in a boat by himself.
# 4. If the sum of the heaviest and lightest person is less than or equal to the limit, then we can send them both in the same boat.
# 5. So, we sort the array and then use 2 pointers to find the answer.

# solution:
# 1. Sort the array.
# 2. Initialize 2 pointers i and j to 0 and n-1 respectively.
# 3. Initialize a variable boats to 0.
# 4. While i is less than or equal to j, do the following:
# 5. If the sum of the heaviest and lightest person is less than or equal to the limit, then we can send them both in the same boat. So, we increment i by 1.
# 6. We decrement j by 1 because we have sent the heaviest person in a boat by himself or with the lightest person.
# 7. We increment boats by 1 because we have sent a boat.
# 8. Return boats.