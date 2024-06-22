class Solution(object):
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        
        # count[i] will store the number of times a prefix sum has occurred
        count = [0] * (n + 1)
        
        # There is one way to have a sum of 0 (by having an empty subarray)
        count[0] = 1
        
        # Initialize the result (number of nice subarrays)
        result = 0
        
        # Initialize the prefix sum (to count the number of odd numbers up to the current index)
        odd_count = 0
        
        # Iterate through the list of numbers
        for num in nums:
            # Increment odd_count if the number is odd
            odd_count += num % 2
            
            # If there have been (odd_count - k) odd numbers before, add the number of times
            # that prefix sum has occurred to the result
            if odd_count - k >= 0:
                result += count[odd_count - k]
            
            # Increment the count of the current prefix sum
            count[odd_count] += 1
        
        return result
