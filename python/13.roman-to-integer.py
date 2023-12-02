#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        r = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        n = 0
        for i, l in enumerate(s):
            roman = r[l]
            if i > 0 and roman > r[s[i - 1]]:
                n -= roman
            else:
                n += roman
        return n


# @lc code=end
