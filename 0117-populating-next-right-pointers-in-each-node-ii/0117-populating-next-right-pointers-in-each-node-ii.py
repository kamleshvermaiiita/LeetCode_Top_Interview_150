"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        q = deque()
        q.append(root)
        
        while q:
            n = len(q)
            rightnext = None
            for i in range(n):
                head = q.popleft()
                head.next = rightnext
                rightnext = head
                if head.right:
                    q.append(head.right)
                if head.left:
                    q.append(head.left)
        
        return root
                
            
        