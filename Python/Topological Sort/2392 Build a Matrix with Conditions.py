class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        order1 = self.generate_topological_sort(rowConditions, k)
        order2 = self.generate_topological_sort(colConditions, k)
        
        if len(order1) < k or len(order2) < k:
            return []
        
        m = {order2[i]: i for i in range(k)}
        ans = [[0] * k for _ in range(k)]
        
        for i in range(k):
            ans[i][m[order1[i]]] = order1[i]
        
        return ans

    def generate_topological_sort(self, A: List[List[int]], k: int) -> List[int]:
        deg = [0] * k
        order = []
        graph = defaultdict(list)
        q = deque()
        
        for c in A:
            graph[c[0] - 1].append(c[1] - 1)
            deg[c[1] - 1] += 1
        
        for i in range(k):
            if deg[i] == 0:
                q.append(i)
        
        while q:
            x = q.popleft()
            order.append(x + 1)
            for y in graph[x]:
                deg[y] -= 1
                if deg[y] == 0:
                    q.append(y)
        
        return order
