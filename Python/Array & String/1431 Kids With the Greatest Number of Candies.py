class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy=max(candies)
        for candy in range(len(candies)):
            if candies[candy]+extraCandies>=max_candy:
                candies[candy]=True
            else:
                candies[candy]=False
        return candies
