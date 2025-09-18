class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        self.tasks = [(-priority, -taskId, userId) for userId, taskId, priority in tasks]
        heapify(self.tasks)
        self.prs = {tid:pr for _, tid, pr in tasks}
        self.usrs = {tid:uid for uid, tid, _ in tasks}
        

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        heappush(self.tasks, (-priority, -taskId, userId))
        self.prs[taskId] = priority
        self.usrs[taskId] = userId
        

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        if newPriority != self.prs[taskId]:
            self.prs[taskId] = newPriority
            heappush(self.tasks, (-newPriority, -taskId, self.usrs[taskId])) 
        

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        self.prs[taskId] = -1
        self.usrs[taskId] = -1
        

    def execTop(self):
        """
        :rtype: int
        """
        if not self.tasks:
            return -1
        pr, tid, uid = heappop(self.tasks)
        pr, tid = -pr, -tid
        while pr != self.prs[tid] or uid != self.usrs[tid]:
            if not self.tasks:
                return -1
            pr, tid, uid = heappop(self.tasks)
            pr, tid = -pr, -tid

        self.rmv(tid)
        return uid
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
