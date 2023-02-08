def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
    players = [(ages[i], scores[i]) for i in range(len(scores))]
    players.sort()

    n = len(scores)
    dp = [0] * n
    res = 0

    for i in range(n):
        dp[i] = players[i][1]
        for j in range(i):
            if players[j][1] <= players[i][1]:
                dp[i] = max(dp[i], dp[j] + players[i][1])
        res = max(res, dp[i])

    return res