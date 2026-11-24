class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.binarySearch(nums,target,True)
        right=self.binarySearch(nums,target,False)
        return[left,right]
    def binarySearch(self,nums,target,leftBias):
        start,end = 0,len(nums)-1
        i=-1
        while(start<=end):
            mid=(start+end)//2
            if target<nums[mid]:
                end=mid-1
            elif target>nums[mid]:
                start=mid+1
            else:
                i=mid
                if leftBias:
                    end= mid-1
                else:
                    start=mid+1
        return i
