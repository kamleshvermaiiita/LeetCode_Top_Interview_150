# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        curr = head
        arr = []
        beforarr = []
        afterarr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
            
        for i in range(len(arr)):
            if arr[i] < x:
                beforarr.append(arr[i])
            else:
                afterarr.append(arr[i])
        
        print(beforarr)
        print(afterarr)
        beforarr.extend(afterarr)
        print(beforarr)
        curr = head
        
        for j in range(len(arr)):
            curr.val = beforarr[j]
            curr = curr.next
        
        return head
        