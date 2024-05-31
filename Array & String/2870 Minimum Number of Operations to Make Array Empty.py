class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        count=0
        for i in nums:
            dic[i]+=1
    
        for ele in dic.keys():
            if dic[ele]==1:
                return -1
            count+=dic[ele]//3
            dic[ele]=dic[ele]%3
            count+=(dic[ele]//2)
            count+=(dic[ele]%2)
        return count
