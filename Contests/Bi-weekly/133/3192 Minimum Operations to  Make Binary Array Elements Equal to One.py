class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_flips = 0
        is_flipped = False

        for index in range(len(nums)):
            if is_flipped:
                current_expected_value = 0
            else:
                current_expected_value = 1

            if nums[index] != current_expected_value:
                num_flips += 1
                is_flipped = not is_flipped

        return num_flips
