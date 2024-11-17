class Node:
    def __init__(self, val):
        self.val = None
        self.next = None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        while head:
            tmp = head.next
            head.next = dummy
            dummy = head
            head = tmp
        # print('head:',head)
        print('dummy:',dummy)
        return dummy