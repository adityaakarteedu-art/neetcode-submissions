class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        size = len(nums)
        found=0
        if size <= 1:
            return False
        else:
           for i in range(1, size):
                if nums[i] == nums[i - 1]:
                    found=1
        if found==1:
            return True
        else:
            return False