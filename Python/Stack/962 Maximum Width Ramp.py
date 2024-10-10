class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        res = -1

        for i in range(len(nums)):
            if stack and nums[stack[-1]] <= nums[i]:
                continue
            stack.append(i)

        print(stack)
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                res = max(res, i - stack[-1])
                stack.pop()
        return res
