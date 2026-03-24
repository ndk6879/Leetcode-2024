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


        '''
        1. find the part
        2. reverse second half
        3. link
        '''

        #1.
        slow , fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #2.
        second = slow.next #second = 3
        slow.next = None
 
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        print(prev)
        first, second = head, prev
        while first and second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1
            first = tmp1 
            second = tmp2