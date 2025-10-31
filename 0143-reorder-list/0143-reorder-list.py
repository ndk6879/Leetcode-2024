# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        

        #1. pointer on the second half
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        print('slow:',slow.val)
        second = slow.next
        slow.next = None
        print('slow:',slow.val)

        #2. reverse second half
        tmp = None
        while second:
            tmp2 = second.next
            second.next = tmp
            tmp = second
            second = tmp2

        #3. reorder
        first, second = head, tmp

        while first and second:
            tmp1, tmp2 = first.next , second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


