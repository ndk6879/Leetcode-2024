# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root: return []

        queue = deque([root])
        ans = [[root.val]]

        while queue:
            tmp = []
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    tmp.append(cur.left.val)
                    queue.append(cur.left)

                if cur.right:
                    tmp.append(cur.right.val)
                    queue.append(cur.right)
            print('ans:',ans)
            if len(tmp) > 0:
                ans.append(tmp)
                
        return ans