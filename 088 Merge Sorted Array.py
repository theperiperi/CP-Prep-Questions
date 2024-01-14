class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last=m+n-1
        a=m-1
        b=n-1

        while b>=0:
            if a>=0 and nums2[b]<nums1[a]:
                nums1[last]=nums1[a]
                a-=1
            else:
                nums1[last]=nums2[b]
                b-=1
            last-=1

                
