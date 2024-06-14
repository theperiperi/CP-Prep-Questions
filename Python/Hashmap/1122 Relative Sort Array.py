class Solution:
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        dic={}
        res=[]
        for i in arr1:
            dic[i]=dic.get(i,0)+1
        
        for i in arr2:
            res+=[i]*dic[i]
            dic.pop(i)
        
        result2 = []
        for key in dic:
            result2 += [key]*dic[key]
        result2.sort()
        return res + result2
        
