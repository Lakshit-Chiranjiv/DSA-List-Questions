# Ninja's Training Problem
# Ninja can train in 3 ways and can't train the same training 2 days in a row
# each training has a profit associated with it for each day
# find the max profit that ninja can earn in n days
# given Nx3 matrix where N is the number of days and 3 is the number of trainings

# recursive solution
def ninjaTrainingRec(points, day, last):
    if day == 0:
        mx = 0
        for i in range(3):
            if i != last:
                mx = max(mx, points[day][i])
        return mx
    mx = 0
    for i in range(3):
        if i != last:
            mx = max(mx, points[day][i] + ninjaTrainingRec(points, day-1, i))
    return mx


# memoization solution
def ninjaTrainingMem(points, day, last, dp):
    if day == 0:
        mx = 0
        for i in range(3):
            if i != last:
                mx = max(mx, points[day][i])
        return mx
    if dp[day][last] != -1:
        return dp[day][last]
    mx = 0
    for i in range(3):
        if i != last:
            mx = max(mx, points[day][i] + ninjaTrainingMem(points, day-1, i, dp))
    dp[day][last] = mx
    return mx


# tabulation solution
def ninjaTrainingTab(points, n):
    dp = [[0 for i in range(4)] for j in range(n)]
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])

    for i in range(1, n):
        for prev in range(4):
            mx = 0
            for j in range(3):
                if j != prev:
                    mx = max(mx, points[i][j] + dp[i-1][j])
            dp[i][prev] = mx
    return dp[n-1][3]


# space optimization
def ninjaTrainingSpace(points, n):
    dp = [0 for i in range(4)]
    dp[0] = max(points[0][1], points[0][2])
    dp[1] = max(points[0][0], points[0][2])
    dp[2] = max(points[0][0], points[0][1])
    dp[3] = max(points[0][0], points[0][1], points[0][2])

    for i in range(1, n):
        temp = [0 for i in range(4)]
        for prev in range(4):
            mx = 0
            for j in range(3):
                if j != prev:
                    mx = max(mx, points[i][j] + dp[j])
            temp[prev] = mx
        dp = temp
    return dp[3]

points = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
n = len(points)
print(ninjaTrainingRec(points, n-1, 3))
dp = [[-1 for i in range(4)] for j in range(n)]
print(ninjaTrainingMem(points, n-1, 3, dp))
print(ninjaTrainingTab(points, n))
print(ninjaTrainingSpace(points, n))
