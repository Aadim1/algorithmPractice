class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = dict()
        
        for i, num in enumerate(nums):
            if num in hashMap:
                if abs(hashMap[num] - i) <= k:
                    return True
                else:
                    hashMap[num] = i
            else:
                hashMap[num] = i
        print(hashMap)
        return False
