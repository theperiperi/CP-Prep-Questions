class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for count in counter.values():
            if count%2!=0:
                return False
        return True
