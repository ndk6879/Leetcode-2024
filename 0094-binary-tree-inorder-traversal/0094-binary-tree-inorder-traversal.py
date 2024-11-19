# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
    
        def dfs(node):
            if not node:
                return
            dfs(node.left)  # 왼쪽 서브트리 탐색
            result.append(node.val)  # 현재 노드 값 추가
            dfs(node.right)  # 오른쪽 서브트리 탐색

        dfs(root)
        return result
        