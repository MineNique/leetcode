#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            one_third = left + (right - left) // 3
            two_thirds = right - (right - left) // 3

            one_third_row, one_third_col = divmod(one_third, n)
            two_thirds_row, two_thirds_col = divmod(two_thirds, n)

            if matrix[one_third_row][one_third_col] == target:
                return True
            elif matrix[two_thirds_row][two_thirds_col] == target:
                return True

            if matrix[one_third_row][one_third_col] > target:
                right = one_third - 1
            elif matrix[two_thirds_row][two_thirds_col] < target:
                left = two_thirds + 1
            else:
                left = one_third + 1
                right = two_thirds - 1

        return False


# @lc code=end
