class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(set(nums))
        count = 0
        left = 0
        freq = defaultdict(int)

        for right in range(len(nums)):
            if nums[right] in freq.keys():
                freq[nums[right]] += 1
            else:
                freq[nums[right]] = 1
            
            while len(freq) == n:
                count += len(nums) - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
        return count
