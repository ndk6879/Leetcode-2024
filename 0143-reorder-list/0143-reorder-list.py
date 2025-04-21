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
        #1. move a pointer to the second half 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None

        
        

        
        #2. reverse the second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        print(prev) 
        
        first, second = head, prev
        #3. reorder
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2