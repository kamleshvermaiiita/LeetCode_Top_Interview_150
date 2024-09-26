class Solution:
    def climbStairs(self, n: int) -> int:
        
        result = [0, 1, 2, 3]
        i = 4
        
        while i<=n:
            ans = result[i-1] + result[i-2]
            result.append(ans)
            i += 1
            
        return result[n]
        
        