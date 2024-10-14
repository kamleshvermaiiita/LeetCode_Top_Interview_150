# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = []
        carry = 0
        mainhead = None
        head = None
        
        while l1 or l2:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            total += carry
            carry = total//10
            total = total%10
            ans.append(total)
            
        if carry:
            ans.append(carry)
        
        for i in range(len(ans)):
            newnode = ListNode(ans[i])
            if not head:
                mainhead = newnode
                head = newnode
            else:
                head.next = newnode
                head = newnode
        
        return mainhead
                
                
                
        