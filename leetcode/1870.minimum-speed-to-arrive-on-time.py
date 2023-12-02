#
# @lc app=leetcode id=1870 lang=python3
#
# [1870] Minimum Speed to Arrive on Time
#

# @lc code=start
from typing import List
import math


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if n >= hour + 1:
            return -1

        left, right = 1, max(max(dist), math.ceil(dist[-1] / (hour + 1 - n)))

        while left < right:
            # Divide the interval into three parts
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3

            # Calculate the time required for each speed
            time1 = sum([math.ceil(d / mid1) for d in dist[:-1]]) + dist[-1] / mid1
            time2 = sum([math.ceil(d / mid2) for d in dist[:-1]]) + dist[-1] / mid2

            # Narrow down the search space
            if time1 <= hour:
                right = mid1
            elif time2 <= hour:
                left = mid1 + 1
                right = mid2
            else:
                left = mid2 + 1

        return left


# @lc code=end
