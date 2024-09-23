class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # Varibles
        rev = 0
        temp = x
        
        
        # Logic
        while x > 0:
            tens = x % 10
            rev = rev*10 + tens
            x = x // 10
        
        if temp == rev:
            return True
        else:
            return False
        
            
        