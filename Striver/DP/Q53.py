# palindrome partitioning II

def isPalindrome(s,i,j):
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True


# recursive solution
def minCut(s,i):
    if i==len(s):
        return 0
    ans = float('inf')
    for j in range(i,len(s)):
        if isPalindrome(s,i,j):
            ans = min(ans,1+minCut(s,j+1))

    return ans


# memoization solution
def minCutMemo(s,i,dp):
    if i==len(s):
        return 0
    if dp[i]!=-1:
        return dp[i]
    ans = float('inf')
    for j in range(i,len(s)):
        if isPalindrome(s,i,j):
            ans = min(ans,1+minCutMemo(s,j+1,dp))
    dp[i] = ans
    return ans

# tabulation solution
def minCutTab(s):
    n = len(s)
    dp = [0]*(n+1)
    dp[n] = 0

    for i in range(n-1,-1,-1):
        ans = float('inf')
        for j in range(i,n):
            if isPalindrome(s,i,j):
                ans = min(ans,1+dp[j+1])
        dp[i] = ans

    return dp[0] - 1

s = "aab"
print(minCut(s,0) - 1)
dp = [-1]*len(s)
print(minCutMemo(s,0,dp) - 1)
print(minCutTab(s))
