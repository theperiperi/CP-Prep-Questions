class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        
        ones_coordinates = [(row, col) for row in range(num_rows) for col in range(num_cols) if grid[row][col] == 1]

        if not ones_coordinates:
            return 0

        min_row = min(row for row, col in ones_coordinates)
        max_row = max(row for row, col in ones_coordinates)
        min_col = min(col for row, col in ones_coordinates)
        max_col = max(col for row, col in ones_coordinates)
        
        return (max_row - min_row + 1) * (max_col - min_col + 1)
