class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = res = 0
        for num in arr:
            res += num
            odd += res % 2
        return (odd + odd * (len(arr) - odd)) % (10 ** 9 + 7)
