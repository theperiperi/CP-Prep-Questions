class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def isMagicSquare(row, col):
            square = [rowSlice[col:col+3] for rowSlice in grid[row:row+3]]
            nums = set()
            for r in square:
                for val in r:
                    if val < 1 or val > 9:
                        return False
                    nums.add(val)
            if len(nums) != 9:
                return False
            target = sum(square[0])
            for i in range(3):
                if sum(square[i]) != target:
                    return False
                if square[0][i] + square[1][i] + square[2][i] != target:
                    return False
            diag1 = square[0][0] + square[1][1] + square[2][2]
            diag2 = square[0][2] + square[1][1] + square[2][0]
            if diag1 != target or diag2 != target:
                return False
            return True

        m = len(grid)
        n = len(grid[0])
        if m < 3 or n < 3:
            return 0
        count = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if isMagicSquare(i, j):
                    count += 1
        return count
