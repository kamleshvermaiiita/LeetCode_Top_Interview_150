class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # Varibles
        n = len(digits)-1
        ans = 0
        final = []
        
        # Logic
        for i in range(0, len(digits)):
            ans = ans*10 + digits[i]
            
        ans += 1
        
        while ans:
            i = ans % 10
            ans = ans // 10
            final.insert(0, i)
        
        return final
            
            
        