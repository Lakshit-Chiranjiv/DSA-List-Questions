class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7

        mp = defaultdict(int)

        for w in words:
            for i,c in enumerate(w):
                mp[(i,c)] += 1

        @cache
        def solve(i,k):
            if i == len(target):
                return 1
            
            if k == len(words[0]):
                return 0

            c = target[i]
            res = solve(i,k+1)
            res += (mp[(k,c)] * solve(i+1,k+1))

            return (res % mod)

        return solve(0,0)
    

# intuition:
# 1. DP will be used to solve this problem.
# 2. The changing parameters here are the index of the current character in the target string and the index of the current character in the words array.
# 3. First of all, we will create a hashmap mp which will store the number of times each character appears at each index in the words array to make the computation faster.
# 4. We will create a recursive function solve(i,k) which returns the number of ways we can form the target string if we are at the ith character of the target string and the kth character of the words array.
# 5. When we reach the end of the target string, we return 1 as we have formed the target string and when we reach the end of the words array, we return 0 as we cannot form the target string.

# solution:
# 1. Create a variable mod and initialize it to 10^9 + 7.
# 2. Create a hashmap mp and initialize it to an empty hashmap.
# 3. Create a for loop which iterates over the words array and in each iteration, we create a for loop which iterates over the current word and in each iteration, we increment mp[(i,c)] by 1.
# 4. Create a recursive function solve(i,k) which returns the number of ways we can form the target string if we are at the ith character of the target string and the kth character of the words array.
# 5. If i == len(target), return 1 as we have reached the end of the target string.
# 6. If k == len(words[0]), return 0 as we have reached the end of the words array.
# 7. Create a variable c and initialize it to the ith character of the target string.
# 8. Create a variable res and initialize it to the result of the recursive call solve(i,k+1) which means we are not taking the kth character of the words array.   
# 9. Update res to res + (mp[(k,c)] * solve(i+1,k+1)). Here, we are taking the kth character of the words array and adding it to the target string.
# 10. Return res % mod.
# 11. Return the result of the recursive call solve(0,0).
