class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[i][j][xor_val] stores count of paths from (i,j) to end with xor_val
        @cache
        def dfs(i: int, j: int, curr_xor: int) -> int:
            if i >= m or j >= n:
                return 0
                
            # Include current cell in XOR
            curr_xor ^= grid[i][j]
            
            # If reached end, check if XOR equals k
            if i == m-1 and j == n-1:
                return 1 if curr_xor == k else 0
            
            # Try both possible moves and sum the paths
            return (dfs(i+1, j, curr_xor) + dfs(i, j+1, curr_xor)) % MOD
            
        return dfs(0, 0, 0)
