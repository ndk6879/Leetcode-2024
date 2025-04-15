# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0: return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                newList = self.mergeList(l1,l2)
                mergedLists.append(newList)
            lists = mergedLists
            
        return lists[0]

        
    def mergeList(self,l1,l2):

        ans = cur = ListNode()

        while l1 and l2:
            if l1.val >= l2.val:
                cur.next = l2
                cur = cur.next
                l2 = l2.next

            else:
                cur.next = l1
                cur = cur.next
                l1 = l1.next

        while l1:
            cur.next = l1
            cur = cur.next
            l1 = l1.next

        while l2:
            cur.next = l2
            cur = cur.next
            l2 = l2.next
        
        return ans.next