class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l, r = 0, len(needle)
        
        while r < len(haystack) + 1:
            if haystack[l:r] == needle:
                return l
            l += 1
            r += 1
            
        return -1
