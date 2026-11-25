class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        for i in range(len(nums)):
            if i==0:
                leftsum=0
            else:
                leftsum+= nums[i-1]
            if leftsum == total - leftsum - nums[i]:
                return i
        return -1