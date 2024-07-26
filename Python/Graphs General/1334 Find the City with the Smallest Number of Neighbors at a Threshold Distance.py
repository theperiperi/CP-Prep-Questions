from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix with infinity
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Distance to itself is 0
        for i in range(n):
            dist[i][i] = 0
        
        # Populate the distance matrix with the given edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Find the city with the smallest number of reachable cities
        # and if there is a tie, choose the city with the greatest number.
        minReachableCities = float('inf')
        bestCity = -1
        
        for i in range(n):
            reachableCities = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    reachableCities += 1
            
            if reachableCities <= minReachableCities:
                minReachableCities = reachableCities
                bestCity = i
        
        return bestCity
