class Solution:
    def countOdds(self, low: int, high: int) -> int:
        answer  = 0
        lowVal = low % 2 == 0 
        highVal = high % 2 == 0
        
        if not lowVal:
            answer += 1
        if not highVal:
            answer += 1
        
        if lowVal and highVal:
            answer += (high - low) // 2
        else:
            answer += (high - low - 1) // 2
        return answer
        
