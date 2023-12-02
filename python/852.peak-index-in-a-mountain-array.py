#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#


# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left < right:
            one_third = left + (right - left) // 3
            two_third = right - (right - left) // 3

            if arr[one_third] < arr[two_third]:
                left = one_third + 1
            else:
                right = two_third - 1

        return left


# @lc code=end
