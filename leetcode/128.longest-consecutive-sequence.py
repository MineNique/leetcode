#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#


# @lc code=start
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:  # Check if it's a starting number of a sequence
                current_num = num
                current_length = 1

                while (
                    current_num + 1 in num_set
                ):  # Find the length of consecutive sequence
                    current_num += 1
                    current_length += 1

                longest = max(longest, current_length)

        return longest


# @lc code=end
