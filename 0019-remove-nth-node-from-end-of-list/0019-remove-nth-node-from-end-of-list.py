# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        tmp = head

        while n:
            tmp = tmp.next
            n -=1

        
        ans = cur = ListNode()
        cur.next = head
        while tmp:
            cur = cur.next
            tmp = tmp.next

        
        cur.next = cur.next.next
        return ans.next
        