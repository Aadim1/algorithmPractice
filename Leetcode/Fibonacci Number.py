class Solution:
    def fib(self, n: int, memo={}) -> int:
        if n == 0: return 0
        if n in memo: return memo[n]
        if n < 2: return 1
        
        memo[n] = self.fib(n-2, memo) + self.fib(n-1, memo)
        return memo[n]
