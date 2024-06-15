class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        n=len(profits)
        projects=[(capital[i],profits[i]) for i in range(n)]
        projects.sort()

        max_heap=[]
        current_capital=w
        project_index=0

        for _ in range(k):
            while project_index<n and projects[project_index][0]<=current_capital:
                heapq.heappush(max_heap,-projects[project_index][1])
                project_index+=1

            if not max_heap:
                break
            
            current_capital+=-heapq.heappop(max_heap)
        return current_capital
