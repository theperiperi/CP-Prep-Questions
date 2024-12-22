class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        # Iterate through all subarrays of length 3
        for i in range(n - 2):
            first = nums[i]
            middle = nums[i + 1]
            third = nums[i + 2]

            # Check the condition
            if middle % 2 == 0 and first + third == middle // 2:
                count += 1

        return count
