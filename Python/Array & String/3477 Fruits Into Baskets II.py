class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 1
        for fruit in fruits:
            b = len(baskets)
            for basket in baskets:
                if basket>=fruit:
                    baskets.remove(basket)
                    break
            if b == len(baskets):
                ans += 1
        return ans-1
