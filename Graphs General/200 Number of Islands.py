class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #checking if grid empty
        if not grid:
            return 0
        
        islands=0
        visited=set()
        rows=len(grid)
        columns=len(grid[0])

        def dfs(r,c):
            if r not in range(rows) or c not in range(columns) or grid[r][c]=="0" or (r,c) in visited:
                return visited
            visited.add((r,c))
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
            
    
        for row in range(rows):
            for column in range(columns):
                if grid[row][column]=="1" and (row,column) not in visited:
                    islands+=1
                    dfs(row,column)
        return islands
