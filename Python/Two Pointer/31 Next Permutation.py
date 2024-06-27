class Solution(object):
    def nextPermutation(self, nums):
        """
        Finds the next lexicographically larger permutation of the given array `nums`
        in-place, modifying the original array.

        Args:
            nums: A list of integers representing the permutation.

        Returns:
            None. The input list `nums` is modified to be the next permutation.
        """

        n = len(nums)

        # Find the first peak (i) from the right where nums[i] < nums[i + 1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # If the array is in descending order, all permutations are exhausted
        if i < 0:
            nums.reverse()
            return

        # Find the first element to the right of peak (i) that's greater than nums[i]
        j = i + 1
        while j < n and nums[j] > nums[i]:
            j += 1

        # Swap nums[i] and nums[j] (in-place)
        nums[i], nums[j - 1] = nums[j - 1], nums[i]

        # Reverse the sub-array from i + 1 to the end (in-place)
        nums[i + 1:] = nums[i + 1:][::-1]
