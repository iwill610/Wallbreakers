# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.D = 0
        def levels(node):
            if not node: 
                return 0
            
            L = levels(node.left)
            R = levels(node.right)
            self.D = max(self.D, L+R)
            
            return max(L, R) + 1

        levels(root)
        return self.D