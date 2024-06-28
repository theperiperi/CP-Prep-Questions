class Solution(object):

    def backtrack(self,candidates,target,start, path, result):
        if target==0:
            result.append(list(path))
            return
        for i in range(start,len(candidates)):
            if i>start and candidates[i]==candidates[i-1]:
                continue
            if candidates[i]>target:
                break
            
            path.append(candidates[i])
            self.backtrack(candidates,target-candidates[i],i+1,path,result)
            path.pop()
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result=[]
        self.backtrack(candidates,target,0,[],result)
        return result
