class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @cache
        def solve(i):
            if i >= n:
                return 0
            
            take = questions[i][0] + solve(i+questions[i][1]+1)
            skip = solve(i+1)

            return max(skip,take)

        return solve(0)

# intuition:
# 1. There are simply two cases for each index, either we take the question or we skip it.
# 2. If we take the question then we add the points of that question and then we skip the questions that are not allowed to be taken.
# 3. If we skip the question then we simply move to the next question.
# 4. DP will allow us to check each case and then we can take the maximum of all the cases.

# solution:
# 1. Take the length of the questions array in a variable n.
# 2. Define a function solve(i) which returns the maximum number of points that can be obtained if we start from index i.
# 3. If i >= n then return 0.
# 4. Take a variable take to store the points if we take the question. Add the points of the current question and then call solve(i+questions[i][1]+1) to skip the questions that are not allowed to be taken.
# 5. Take a variable skip to store the points if we skip the question. Call solve(i+1) to move to the next question.
# 6. Return max(skip,take).
# 7. Finally call solve(0) and return the answer.

# Time Complexity: O(n) where n is the length of the questions array. This is because we are using dp and memoization to store the results of the subproblems and hence we are not repeating the calculations. We only visit each index once.

# Space Complexity: O(n) where n is the length of the questions array. This is because we are using dp and memoization to store the results of the subproblems.