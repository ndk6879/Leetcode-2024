# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ans = dummy = ListNode(0,head)

        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            dummy = dummy.next

        print(dummy.val)
        dummy.next = dummy.next.next

        return ans.next