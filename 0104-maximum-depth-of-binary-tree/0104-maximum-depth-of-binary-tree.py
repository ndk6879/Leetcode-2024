# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        queue = deque([])
        queue.append(root)
        ans = 0
        if not root: return 0
        while(queue):
            tmp = []
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                tmp.append(cur.val)
            ans += 1
        return ans    
                