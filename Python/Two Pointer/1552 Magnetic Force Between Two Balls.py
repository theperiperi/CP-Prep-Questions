class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type mid: int
        :rtype: int
        """
        position.sort()
        left,right = 0, max(position)
        while right>left+1:
            mid=(left+right)//2
        
            prev=position[0]
            count =1
            for each in position:
                if each-prev>=mid:
                    prev=each
                    count+=1
        
            if count>=m:
                left=mid 
            else:
                right=mid
        return left      
