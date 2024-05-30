class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        #works on the property that xor or array-xor of consecutive part=xor of the prefix
        
        n=len(arr)
        prefix=[0]*(n+1)

        #computing xor from first index to array index, stored in prefix
        for i in range(n):
            prefix[i+1]=prefix[i]^arr[i]
        
        count=0
        for i in range(n):
            for k in range(i+1,n):
                if prefix[i]==prefix[k+1]:
                    count+=(k-i)
        
        return count

        
