# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

#        아래 두줄로 나눠 선언하면 ans,dummy가 다른 ListNode를 가르키는거임 그래서 한줄로 합쳐야함
        # ans = ListNode(0, head)
        # dummy = ListNode(0, head)     
        ans = dummy = ListNode(0,head)        

        #1. head를 n만큼 앞에서 옮긴다.
        for _ in range(n):
            head = head.next
        
        while head:
            dummy = dummy.next
            head = head.next
        
        dummy.next = dummy.next.next
        print(head)
        return ans.next