# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        arr1 = []
        
        while curr:
            arr1.append(curr.val)
            curr = curr.next
        
        reminder = len(arr1)%k
        multiple = len(arr1)//k
        n = len(arr1) - reminder
        arr2 = arr1[:n]
        
        for i in range(multiple):
            arr3 = arr2[i*k:i*k+k][::-1]
            print(arr3)
            arr1[i*k:i*k+k] = arr3
        
        curr = head
        for i in range(len(arr1)):
            curr.val = arr1[i]
            curr = curr.next
            
        return head
            
        