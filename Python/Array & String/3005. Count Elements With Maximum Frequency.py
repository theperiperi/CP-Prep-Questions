class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = [0] * 101
        mx = 0
        res = 0
        for num in nums:
            freq[num] += 1
            f = freq[num]
            if f > mx:
                mx = f
                res = f
            elif f == mx:
                res += f
        return res
