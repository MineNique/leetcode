#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List
from math import sqrt


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        step = int(sqrt(n))
        prev, curr = 0, 0

        while curr < n and nums[curr] < target:
            prev = curr
            curr += step

        curr = min(curr, n - 1)

        for i in range(prev, curr + 1):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i

        return curr + 1


# @lc code=end
