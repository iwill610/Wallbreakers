# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        compare1=[]
        compare2=[]
        def check(node,comparelist):
            if node:
                
                if not node.left and not node.right:
                    comparelist.append(node.val)
                check(node.left,comparelist)
                check(node.right,comparelist)
        check(root1,compare1)
        check(root2,compare2)
        return compare1==compare2