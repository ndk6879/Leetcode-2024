# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        #1. merge two sub lists in lists arr
        #2. update the lists with those two sub lists

        if not lists:
            return None


        while len(lists) > 1:
            sub = []
            for i in range(0,len(lists),2):
                
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None

                sub.append(self.mergeLists(l1,l2))
            lists = sub
        return lists[0]

        
    def mergeLists(self,l1,l2):

        ans = cur = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next

            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next

        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next

        return ans.next

                
        

