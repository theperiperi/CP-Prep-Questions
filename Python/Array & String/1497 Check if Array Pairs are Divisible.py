class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_store=[0]*k

        for num in arr:
            remainder=num%k
            remainder_store[remainder]+=1
        
        if remainder_store[0] % 2 != 0:
            return False
        
        for i in range(1, k):
            if remainder_store[i] != remainder_store[k - i]:
                return False
        
        return True
