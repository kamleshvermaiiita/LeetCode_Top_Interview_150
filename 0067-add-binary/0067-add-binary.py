class Solution:
    
    def addBinary(self, a: str, b: str) -> str:
        # Varibles
        Decimal_a = int(a, 2)
        Decimal_b = int(b, 2)
        
        total = Decimal_a + Decimal_b
        ans = format(total, 'b')
        #print(ans)
        
        return ans
            
        