#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#


# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                res.append(path[:])  # Append a copy of the current path to the result
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue

                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

        res = []
        backtrack(0, target, [])
        return res


# @lc code=end
