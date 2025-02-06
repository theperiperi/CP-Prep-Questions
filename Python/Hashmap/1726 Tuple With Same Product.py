class Solution(object):
    def tupleSameProduct(self, nums):
        n = len(nums)
        map = {}
        for i in range(n):
            for j in range(i+1, n):
                temp = nums[i] * nums[j]
                if temp in map:
                    map[temp] += 1
                else:
                    map[temp] = 1
        ans = 0
        for i in map.values():
            if i > 1:
                ans += 8 * i * (i-1) / 2
        return ans
