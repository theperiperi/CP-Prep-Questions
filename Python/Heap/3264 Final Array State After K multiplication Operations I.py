class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap=[(value,index) for index, value in enumerate(nums)]
        heapify(heap)
        for thing_index in range(k):
            value, index= heap[0]
            heapreplace(heap,(value*multiplier,index))
        for value, index in heap:
            nums[index]=value
        return nums
