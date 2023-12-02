#
# @lc app=leetcode id=920 lang=python3
#
# [920] Number of Music Playlists
#


# @lc code=start
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9 + 7
        dp = {}

        def count(curGoal, oldSong):
            if curGoal == 0 and oldSong == n:
                return 1
            if curGoal == 0 or oldSong > n:
                return 0
            if (curGoal, oldSong) in dp:
                return dp[(curGoal, oldSong)]

            res = (n - oldSong) * count(curGoal - 1, oldSong + 1)  # New Song
            if oldSong > k:
                res += (oldSong - k) * count(curGoal - 1, oldSong)  # Old Song

            dp[(curGoal, oldSong)] = res % mod
            return dp[(curGoal, oldSong)]

        return count(goal, 0)


# @lc code=end
