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
        
        #1. find mid pointer
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next

        #맨마지막에 오는 3의 next를 none으로 만듬. example 2에
        slow.next = None #example1에선 2가 slow고 .next를해서 first half를 3과 연결끊음.
        prev = None


        #2. reverse the second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        print(prev)


        #3. link

        first, second = head, prev
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        