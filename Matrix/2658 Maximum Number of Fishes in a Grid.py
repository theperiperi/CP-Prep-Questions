class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if (r,c) not in unseen:return 0
            unseen.remove((r,c))
            return grid[r][c] + dfs(r+1,c)+dfs(r,c+1)+dfs(r-1,c)+dfs(r,c-1)
            
        m, n, ans = len(grid), len(grid[0]), 0
        #set
        unseen = {(i,j) for i,j in product(range(m),range(n))
                                                if grid[i][j]}
        while unseen: ans = max(ans,dfs(*min(unseen)))

        return ans 


#or

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]>0:
                    ans=max(ans,self.dfs(i,j,grid,n,m))
        return ans

    def dfs(self,i:int,j:int,grid:List[List[int]],n:int,m:int) -> int:
        f=grid[i][j]
        grid[i][j]=0
        dr=[0,1,0,-1,0]
        for k in range(4):
            nr=i+dr[k]
            nc=j+dr[k+1]
            if nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc]>0:
                f+=self.dfs(nr,nc,grid,n,m)
        return f
