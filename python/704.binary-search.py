#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return nums.index(target) if target in nums else -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


# @lc code=end
