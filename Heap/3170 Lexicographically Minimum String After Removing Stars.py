class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        for i,c in enumerate(s):
            if c=='*':
                heappop(heap)
            else:
                heappush(heap,(ord(c),-i))
        
        ans = ['']*len(s)
        while heap:
            ordChar,i = heappop(heap)
            ans[-i] = chr(ordChar)
            
        return ''.join(ans)
