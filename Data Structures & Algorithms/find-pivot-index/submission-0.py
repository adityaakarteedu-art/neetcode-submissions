class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        for i in range(len(nums)):
            leftsum=sum(nums[0:i])
            if leftsum==total-leftsum-nums[i]:
                return i
        return -1