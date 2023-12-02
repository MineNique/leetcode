#
# @lc app=leetcode id=2616 lang=python3
#
# [2616] Minimize the Maximum Difference of Pairs
#


# @lc code=start
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def can_form_pairs(mid):
            count = 0
            i = 0
            while i < len(nums) - 1 and count < p:
                if nums[i + 1] - nums[i] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p

        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                right = mid
            else:
                left = mid + 1

        return left


# @lc code=end
