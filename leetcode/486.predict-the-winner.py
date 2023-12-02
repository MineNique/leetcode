#
# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#

# @lc code=start
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        arr = [0] * (n := len(nums))
        for i in range(n - 1, -1, -1):
            arr[i] = nums[i]
            for j in range(i + 1, n):
                arr[j] = max(nums[i] - arr[j], nums[j] - arr[j - 1])
        return arr[n - 1] >= 0


# @lc code=end
