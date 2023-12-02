#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#


# @lc code=start
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Time O(log n)
        count = {}
        for path in paths:
            cityA, cityB = path


# @lc code=end
