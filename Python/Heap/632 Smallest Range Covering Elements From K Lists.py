class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap=[]
        curr_max=float('-inf')
        for i in range(len(nums)):
            heapq.heappush(heap,(nums[i][0],i,0))
            curr_max=max(curr_max,nums[i][0])
        small=[float('-inf'),float('inf')]
        while heap:
            curr_min, list_idx, i=heapq.heappop(heap)
            if (((curr_max-curr_min)<(small[1]-small[0])) or((curr_max-curr_min)==(small[1]-small[0])) and curr_min <small[0]):
                small=[curr_min,curr_max]
            if i+1<len(nums[list_idx]):
                nxt=nums[list_idx][i+1]
                heapq.heappush(heap,(nxt,list_idx,i+1))
                curr_max=max(curr_max,nxt)
            else:
                break
        return small
