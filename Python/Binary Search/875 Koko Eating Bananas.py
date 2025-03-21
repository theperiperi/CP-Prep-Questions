class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        def canEat(k):
            ans = 0
            for pile in piles:
                ans += ceil (pile/k)
            if ans<=h:
                return True
            return False
        while left <= right:
            mid = (left + right)//2
            if canEat(mid):
                right = mid -1
            else:
                left = mid +1
        return left
