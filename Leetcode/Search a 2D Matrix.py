class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if target in matrix[mid]:
                return True
            
            if matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
