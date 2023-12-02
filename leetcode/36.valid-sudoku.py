#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#


# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrids = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    if (
                        num in rows[i]
                        or num in cols[j]
                        or num in subgrids[3 * (i // 3) + (j // 3)]
                    ):
                        return False
                    rows[i].add(num)
                    cols[j].add(num)
                    subgrids[3 * (i // 3) + (j // 3)].add(num)

        return True


# @lc code=end
