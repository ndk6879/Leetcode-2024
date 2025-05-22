# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        ans = 0
        queue = deque([root]) 
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.right:
                    queue.append(cur.right)

                if cur.left:
                    queue.append(cur.left)
            ans +=1

        return ans