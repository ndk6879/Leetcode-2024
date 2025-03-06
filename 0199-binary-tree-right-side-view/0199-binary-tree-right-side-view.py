# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = [root.val]
        queue = deque([root])

        while queue:
            tmp = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    tmp.append(cur.left.val)
                    queue.append(cur.left)

                if cur.right:
                    tmp.append(cur.right.val)
                    queue.append(cur.right)

            if tmp:
                ans.append(tmp[-1])

        return ans