class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        flip = 0
        flipped = [0] * n
        count = 0
        
        for i in range(n):
            if i >= k:
                flip ^= flipped[i - k]
            if flip % 2 == nums[i]:
                if i + k > n:
                    return -1
                flip ^= 1
                flipped[i] = 1
                count += 1
        
        return count
