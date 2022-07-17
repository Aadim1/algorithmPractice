class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        
        while r < len(nums) - 1:
            
            if nums[l] == nums[r]:
                if nums[r] == nums[r + 1]:
                    while r + 1 < len(nums) and nums[r] == nums[r+ 1]:
                        nums.pop(r + 1)
            l += 1
            r += 1
        return len(nums)
