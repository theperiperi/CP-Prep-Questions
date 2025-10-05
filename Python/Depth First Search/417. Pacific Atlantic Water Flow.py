class Solution(object):
    def pacificAtlantic(self, heights):
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(row, col, ocean):
            if (row, col) not in ocean:
                ocean.add((row, col))

                if(row > 0):
                    if heights[row - 1][col] >= heights[row][col]:
                        dfs(row - 1, col, ocean)
                
                if(row < rows - 1):
                    if heights[row + 1][col] >= heights[row][col]:
                        dfs(row + 1, col, ocean)
                
                if(col > 0):
                    if heights[row][col - 1] >= heights[row][col]:
                        dfs(row, col - 1, ocean)
                
                if(col < cols - 1):
                    if heights[row][col + 1] >= heights[row][col]:
                        dfs(row, col + 1, ocean)

        for i in range(0, cols):
            dfs(0, i, pacific)
            dfs(rows - 1, i, atlantic)
        
        for j in range(0, rows):
            dfs(j, 0, pacific)
            dfs(j, cols - 1, atlantic)

        return list(pacific.intersection(atlantic))
