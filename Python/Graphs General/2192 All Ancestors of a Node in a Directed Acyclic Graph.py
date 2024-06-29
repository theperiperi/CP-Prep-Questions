class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        graph=defaultdict(list)
        in_degree=[0]*n
        for u,v in edges:
            graph[u].append(v)
            in_degree[v]+=1

        
        topo_order=[]
        queue=deque([i for i in range(n) if in_degree[i]==0])
        while queue:
            node=queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor]-=1
                if in_degree[neighbor]==0:
                    queue.append(neighbor)

        ancestors=[set() for _ in range(n)]
        for node in topo_order:
            for neighbor in graph[node]:
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)
        
        result= [sorted(list(ancestor_set)) for ancestor_set in ancestors]
        return result
