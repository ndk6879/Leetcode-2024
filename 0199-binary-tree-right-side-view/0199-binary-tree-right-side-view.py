# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        from collections import deque
        if not root: return []
        queue = deque([root])

        ans = [root.val]
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                    level.append(cur.left.val)

                if cur.right:
                    queue.append(cur.right)
                    level.append(cur.right.val)

            if level:
                ans.append(level[-1])
        return ans