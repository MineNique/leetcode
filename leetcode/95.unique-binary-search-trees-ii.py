#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = bisect_left(nums, True, key=lambda x: x < nums[0])

        if target >= nums[0]:
            left = bisect_left(nums, target, hi=k - 1)
            return left if nums[left] == target else -1

        rght = bisect_left(nums, target, lo=k)
        return rght if rght < len(nums) and nums[rght] == target else -1


# @lc code=end
