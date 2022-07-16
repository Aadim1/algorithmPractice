def twoSum(self, nums: list[int], target: int) -> list[int]:
        pointer1 = 0
        pointer2 = len(nums) - 1
        
        
        while pointer1 < pointer2:
            s = nums[pointer1] + nums[pointer2]
            if s == target:
                return [pointer1, pointer2]
            elif s < target:
                pointer1 += 1
            else:
                pointer2 -= 1