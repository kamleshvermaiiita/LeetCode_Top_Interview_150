class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # Logic --> using split function
        l = s.split()
        
        if len(l) == 0:
            return 0
        else:
            return len(l[-1])
            
        
        