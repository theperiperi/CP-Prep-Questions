class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

        def binary_search(nums,target,is_searching_left):
            start=0
            end=len(nums)-1
            idx=-1

            while start<=end:
                mid=(start+end)//2
                if nums[mid]>target:
                    end=mid-1
                elif nums[mid]<target:
                    start=mid+1
                
                else:
                    idx=mid
                    if is_searching_left:
                        end=mid-1
                    else:
                        start=mid+1
            return idx

        one=binary_search(nums,target,True)
        two=binary_search(nums,target,False)

        return [one, two]
