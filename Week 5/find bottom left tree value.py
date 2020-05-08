# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return node.val