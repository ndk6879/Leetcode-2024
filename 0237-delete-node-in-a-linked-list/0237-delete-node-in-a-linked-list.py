class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: None
        """
        # 현재 노드의 값을 다음 노드의 값으로 바꾼다
        node.val = node.next.val
        # 현재 노드의 다음 포인터를 다음 다음 노드로 연결한다
        node.next = node.next.next
