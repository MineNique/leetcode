#
# @lc app=leetcode id=2141 lang=python3
#
# [2141] Maximum Running Time of N Computers
#

# @lc code=start
from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        extra = sum(batteries[:-n])
        batteries = batteries[-n:]

        prefix = 0
        for i, x in enumerate(batteries):
            prefix += x
            if i + 1 < len(batteries) and batteries[i + 1] * (i + 1) - prefix > extra:
                return (prefix + extra) // (i + 1)
        return (prefix + extra) // n


# @lc code=end
