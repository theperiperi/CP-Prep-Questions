class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        cols = [[row[column] for row in grid] for column in range(len(grid[0]))]
        res=0
        for col in cols:
            index=0
            while index<len(col)-1:
                diff= col[index+1]-col[index]
                if diff<=0:
                    col[index+1] = col[index]+1
                    res+=(-1*diff+1)
                index+=1
        return res
