"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        hashmap = {}
        currentpointer = head
        while currentpointer:
            newnode = Node(currentpointer.val)
            hashmap[currentpointer] = newnode
            currentpointer = currentpointer.next
            
        currentpointer = head
        while currentpointer:
            hashmap[currentpointer].next = hashmap.get(currentpointer.next)
            hashmap[currentpointer].random = hashmap.get(currentpointer.random)
            currentpointer = currentpointer.next
        
        return hashmap[head]
        