class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        visited = set()
        adjMatrix = defaultdict(list)
        stonesSet = set()
        for x, y in stones:
            adjMatrix[x].append(y)
            adjMatrix[y].append(x)
            stonesSet.add((x, y))
        self.removed = 0

        def dfs(x, y):
            visited.add((x, y))
            self.removed += 1
            for j in adjMatrix[x]:
                if (x, j) not in visited and (x, j) in stonesSet:
                    dfs(x, j)

            for i in adjMatrix[y]:
                if (i, y) not in visited  and (i, y) in stonesSet:
                    dfs(i, y)

        
        for i,j in stones:
                if (i, j) not in visited:                    
                    dfs(i, j)
                    self.removed -= 1
        
        return self.removed
