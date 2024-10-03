class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p

        if remainder == 0:
            return 0

        prefix_mod_map = {0: -1}
        prefix_sum = 0
        min_length = len(nums)

        for i, num in enumerate(nums):
            prefix_sum += num
            current_mod = prefix_sum % p
            target_mod = (current_mod - remainder + p) % p

            if target_mod in prefix_mod_map:
                min_length = min(min_length, i - prefix_mod_map[target_mod])

            prefix_mod_map[current_mod] = i

        return min_length if min_length < len(nums) else -1
