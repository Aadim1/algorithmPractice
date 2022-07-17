class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashSet = set()
        
        # [1,1,2,3,4]
        # [1,2,3,4,_]
        numsLen = len(nums)
        
       
        i = 0 
        while i < len(nums):
            if nums[i] in hashSet:
                nums.pop(i)
                i -= 1
            else:
                hashSet.add(nums[i])
            i += 1
        
        return len(nums)
            
