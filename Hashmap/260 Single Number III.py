class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic=defaultdict(int)
        ans=[]
        for i in nums:
            dic[i]+=1
        for i in dic.keys():
            if dic[i]==1:
                ans.append(i)
        return ans
