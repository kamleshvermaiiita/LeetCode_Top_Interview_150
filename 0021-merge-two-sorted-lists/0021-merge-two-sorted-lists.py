# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = []
        head = None
        mainhead = None
        
        while list1 or list2:
            if list1:
                ans.append(list1.val)
                list1 = list1.next
            if list2:
                ans.append(list2.val)
                list2 = list2.next
        
        ans.sort()
        for i in range(len(ans)):
            newnode = ListNode(ans[i])
            if not head:
                head = newnode
                mainhead = newnode
            else:
                head.next = newnode
                head = newnode
        
        return mainhead
            
            
        