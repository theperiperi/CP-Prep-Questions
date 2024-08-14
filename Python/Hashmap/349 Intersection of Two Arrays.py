class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ddict=defaultdict(int)
        for num in nums1:
            ddict[num]+=1
        res=[]

        for num in nums2:
            if num in ddict:
                res.append(num)
                del ddict[num]

        return res
