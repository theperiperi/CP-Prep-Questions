class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs (vertice, res):
            if vertice in seen:
                return 
            seen.add(vertice)
            res.append(vertice)

            for neighbor in adj[vertice]:
                dfs(neighbor, res)
            
            return res
        
        adj = defaultdict(list)
        for vertice1, vertice2 in edges:
            adj[vertice1].append(vertice2)
            adj[vertice2].append(vertice1)
        
        res = 0
        seen = set()

        for vertice in range(n):
            if vertice in seen:
                continue
            component = dfs(vertice, [])
            flag = True
            for vertice2 in component:
                if len(component) - 1 != len(adj[vertice2]):
                    flag = False
                    break
            if flag:
                res += 1
        
        return res
