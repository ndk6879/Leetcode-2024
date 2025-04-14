# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        dummy = None

        while cur:
            tmp = cur.next
            cur.next = dummy
            dummy = cur
            cur = tmp
            # print(dummy.val, cur.val)

        return dummy