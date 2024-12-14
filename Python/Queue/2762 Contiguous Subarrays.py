class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:      
        queue_max, queue_min = deque(), deque()
        left, ans = 0, 0
        for i, num in enumerate(nums):
            
            while queue_max and num > nums[queue_max[-1]]:
                queue_max.pop()
            queue_max.append(i)

            while queue_min and num < nums[queue_min[-1]]:
                queue_min.pop()
            queue_min.append(i)

            while nums[queue_max[0]] - num > 2:
                queue_max.popleft()
                left = queue_max[0]
            while num - nums[queue_min[0]] > 2:
                queue_min.popleft()
                left = queue_min[0]

            ans += i - left + 1
        return ans
