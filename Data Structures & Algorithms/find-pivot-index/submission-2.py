class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        for i in range(len(nums)):
            if i==0:
                leftsum=0
                rightsum=total-nums[0]
            else:
                leftsum+= nums[i-1]
                rightsum = rightsum - nums[i]
            if leftsum == rightsum:
                return i
        return -1