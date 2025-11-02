# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        tmp = ans = ListNode()
        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val >= l2.val:
                tmp.next = l2
                l2 = l2.next
            
            else:
                tmp.next = l1
                l1 = l1.next
            tmp = tmp.next

        tmp.next = l1 or l2
        
        return ans.next