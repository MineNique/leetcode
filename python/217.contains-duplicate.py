#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        list_hash = set()
        for i in nums:
            if i in list_hash:
                return True
            else:
                list_hash.add(i)
        return False


# @lc code=end
