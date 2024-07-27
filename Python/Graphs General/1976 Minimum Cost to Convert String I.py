class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        MAX,ordA,res = float('inf'),ord('a'),0
        graph = [[MAX]*26 for _ in range(26)]
        originalSet,changedSet = set(),set()

        for x,y,c in zip(original,changed,cost):
            ordX,ordY = ord(x)-ordA,ord(y)-ordA
            graph[ordX][ordY] = min(graph[ordX][ordY],c)
            originalSet.add(ordX)
            changedSet.add(ordY)

        commonSet = originalSet.intersection(changedSet)

        for k in commonSet:
            for i in originalSet:
                for j in changedSet:
                    graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j]) 

        for s,t in zip(source,target):
            if s == t: continue
            ordS,ordT = ord(s)-ordA,ord(t)-ordA
            if graph[ordS][ordT] == MAX: return -1
            res+=graph[ordS][ordT]
            
        return res         
        
