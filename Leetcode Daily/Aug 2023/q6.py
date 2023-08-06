class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9+7
        @cache
        def number_of_playlists(i, j):
            if i == 0 and j == 0:
                return 1
            if i == 0 or j == 0:
                return 0
            ans = (number_of_playlists(i - 1, j - 1) * (n - j + 1)) % MOD
            if j > k:
                ans += (number_of_playlists(i - 1, j) * (j - k)) % MOD
                ans %= MOD
            return ans

        return number_of_playlists(goal, n)