class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(current_permutation,used):
            if len(current_permutation)==len(nums):
                result.append(list(current_permutation))
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    current_permutation.append(nums[i])
                    used[i]=True

                    backtrack(current_permutation,used)
                    used[i]=False
                    current_permutation.pop()

        result=[]
        backtrack([],[False]*len(nums))
        return result
