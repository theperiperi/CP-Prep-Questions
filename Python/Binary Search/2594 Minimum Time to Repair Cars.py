class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left , right = 1, min(ranks) * cars * cars
        ans = right

        while left <= right:
            mid = (left + right) // 2
            total_cars = sum (math.floor(math.sqrt(mid//r)) for r in ranks)

            if total_cars >= cars:
                ans = mid 
                right = mid - 1
            else:
                left = mid + 1
        return ans
