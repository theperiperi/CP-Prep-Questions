from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        while matrix:
            # top row
            ans.extend(matrix.pop(0))

            # right column
            if matrix and matrix[0]:
                for row in matrix:
                    ans.append(row.pop(-1))

            # bottom row reverse
            if matrix and matrix[0]:
                ans.extend(reversed(matrix.pop(-1)))

            # left column reversed
            if matrix and matrix[0]:
                for row in reversed(matrix):
                    ans.append(row.pop(0))

        return ans
