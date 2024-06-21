class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """

        res=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                res+=customers[i]
                customers[i]=0
        
        
        if len(customers)<minutes:
            return res

        #now array has only number of customers we lose
        start=0
        end=minutes
        max_count=sum(customers[i] for i in range(start,end))
        count=max_count
        
        while end<len(customers):
            count-=customers[start]
            start+=1
            count+=customers[end]
            end+=1
            max_count=max(count,max_count)
            
        
        res+=max_count
        return res
