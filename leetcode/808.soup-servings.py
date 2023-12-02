#
# @lc app=leetcode id=808 lang=python3
#
# [808] Soup Servings
#

# @lc code=start


class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0
        n = (n + 24) // 25
        memo = dict()

        def dynamic(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i <= 0 and j <= 0:
                return 0.5
            if i <= 0:
                return 1.0
            if j <= 0:
                return 0.0
            memo[(i, j)] = 0.25 * (
                dynamic(i - 4, j)
                + dynamic(i - 3, j - 1)
                + dynamic(i - 2, j - 2)
                + dynamic(i - 1, j - 3)
            )
            return memo[(i, j)]

        return dynamic(n, n)


# @lc code=end
