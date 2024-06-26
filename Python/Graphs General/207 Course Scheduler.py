class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph=defaultdict(list)
        in_degree=[0]*numCourses

        for course,prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course]+=1
        
        zero_queue=deque([course for course in range(numCourses) if in_degree[course]==0])
        count=0

        while zero_queue:
            course=zero_queue.popleft()
            count+=1

            for neighbor in graph[course]:
                in_degree[neighbor]-=1
                if in_degree[neighbor]==0:
                    zero_queue.append(neighbor)
        return count==numCourses
