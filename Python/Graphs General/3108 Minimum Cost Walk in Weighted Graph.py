class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Initialize parent array for union-find
        parent = list(range(n))
        min_edge_cost = [-1] * n

        # Find the root of a node with path compression
        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        # Union operation with minimum path cost update
        for u, v, cost in edges:
            root_u = find(u)
            root_v = find(v)

            min_edge_cost[root_v] &= cost

            if root_u != root_v:
                min_edge_cost[root_v] &= min_edge_cost[root_u]
                parent[root_u] = root_v

        # Process the queries
        results = []
        for start, end in queries:
            if start == end:
                results.append(0)
            elif find(start) != find(end):
                results.append(-1)
            else:
                results.append(min_edge_cost[find(start)])

        return results
