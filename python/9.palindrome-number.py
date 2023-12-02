#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return x == int("".join(reversed(str(x))))


# @lc code=end
