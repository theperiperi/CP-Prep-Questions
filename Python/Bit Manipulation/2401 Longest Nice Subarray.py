class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 1

        start = 0
        bit_mask = 0

        for end in range(n):
            while bit_mask & nums[end] != 0:
                bit_mask ^= nums[start]
                start += 1
            
            bit_mask |= nums[end]
            max_len = max(max_len, end - start + 1)

        return max_len
