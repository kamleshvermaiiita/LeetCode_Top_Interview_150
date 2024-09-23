class Solution:
    def isValid(self, s: str) -> bool:
        
        # Variables
        stack = []
        d = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        
        # Logic
        for i in range(0, len(s)):            
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])            
            else:
                n = len(stack) - 1                
                if len(stack) == 0:
                    return False                
                elif d[s[i]] != stack[n]:
                    return False
                else:
                    stack.pop()
        
        if len(stack) == 0:
            return True
        else:
            return False
                
        