class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # Variables
        n1 = len(haystack)
        n2 = len(needle)
        
        # Base Condition
        if n2 == 0:
            return 0
        if n1 < n2:
            return -1
        
        # Logic
        for i in range(n1-n2+1):
            if haystack[i:i+n2] == needle:
                return i
        
        return -1
            
        