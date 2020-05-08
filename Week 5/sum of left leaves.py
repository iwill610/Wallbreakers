# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def count(tree):
            if tree:
                total=0
                if tree.left and not tree.left.left and not tree.left.right:
                    total+=tree.left.val
                
                total+=count(tree.left)
                total+=count(tree.right)
                return total
            else:
                return 0
        
        return count(root)