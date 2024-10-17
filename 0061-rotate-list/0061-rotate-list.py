# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k == 0 or not head :
            return head
        
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
            
        i = 0
        m = k % len(arr)
        n = len(arr) - m
        while i < n:
            arr.append(arr[0])
            arr.pop(0)
            i += 1
        
        curr = head
        for j in range(len(arr)):
            curr.val = arr[j]
            curr = curr.next
            
        return head
        
            
        