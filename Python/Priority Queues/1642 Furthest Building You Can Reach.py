class Solution:
    def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
        #aka minimum heap
        priority_queue = []  
        for i in range(len(h) - 1):
            diff = h[i+1] - h[i]
            #fall down, no moves wasted
            if diff <= 0: 
                continue
            heapq.heappush(priority_queue, diff)
            #ladders ho gaya, use bricks kanna
            if len(priority_queue) > l:  
                b -= heapq.heappop(priority_queue)
            if b < 0:  # out of bricks
                return i

        #incase there are still remaining bricks/ladders u can traverse entire building
        return len(h) - 1
