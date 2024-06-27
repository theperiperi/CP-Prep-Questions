class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(remaining_target,current_combination,start_index):
            if remaining_target==0:
                result.append(list(current_combination))
                return
            
            if remaining_target<0:
                return
            
            for i in range(start_index,len(candidates)):
                candidate=candidates[i]
                current_combination.append(candidate)
                backtrack(remaining_target-candidate,current_combination,i)
                current_combination.pop()

        candidates.sort()
        result=[]
        backtrack(target,[],0)
        return result
