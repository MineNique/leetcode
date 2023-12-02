#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc code=start
from typing import DefaultDict, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = DefaultDict(list)  # mapping charCount -> list of Anagrams

        for s in strs:
            count = [0] * 26  # For a, b, c,... ,z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()


# @lc code=end
