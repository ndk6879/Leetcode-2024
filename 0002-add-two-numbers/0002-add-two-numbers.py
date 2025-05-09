# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        ans = cur = ListNode()
        while carry or l1 or l2:
            
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            value = v1 + v2 + carry
            val = value % 10
            carry = value // 10
            cur.next = ListNode(val)
            cur = cur.next
            print(cur.val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return ans.next
