# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = dummy = ListNode()

        carry = 0
        while l1 and l2 :
            val = l1.val + l2.val + carry

            value = val % 10
            carry = val // 10

            cur.next = ListNode(value)
            print('cur:',cur)

            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        
        while l1:
            cur.next = ListNode(l1.val)
            l1 = l1.next
            cur = cur.next

        while l2:
            cur.next = ListNode(l2.val)
            l2 = l2.next
            cur = cur.next

        if carry:
            cur.next = ListNode(carry)
            cur = cur.next
        
        return dummy.next