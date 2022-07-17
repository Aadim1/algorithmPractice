class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(number: int, memo={}):
            if number <= 3:
                return number
            
            if number in memo:
                return memo[number]
            
            memo[number] = helper(number - 1, memo) + helper(number - 2, memo)
            return memo[number]
        
        return helper(n)
