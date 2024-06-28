class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        degree=[0]*n

        #counting degree
        for road in roads:
            degree[road[0]]+=1
            degree[road[1]]+=1

        #sort cities by degree
        sorted_cities=sorted(degree,reverse=True)

        #calc importance
        total_importance=0
        for i in range(n):
            total_importance+=sorted_cities[i]*(n-i)
        return total_importance
