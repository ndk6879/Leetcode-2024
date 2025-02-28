# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ans = dummy = ListNode(0,head)        

        #1. head를 n만큼 앞에서 옮긴다.
        for _ in range(n):
            head = head.next
        
        while head:
            dummy = dummy.next
            head = head.next
        
        dummy.next = dummy.next.next
        print(head)
        return ans.next