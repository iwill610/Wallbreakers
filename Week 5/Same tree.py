# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        contp=[]
        contq=[]
        def vals(tree,container):
            if tree:
                container.append(tree.val)
                if tree.left:   
                    vals(tree.left,container)
                else:
                    container.append("nullleft")
                if tree.right:
                    vals(tree.right,container)
                else:
                    container.append('nullright')
        vals(p,contp)
        vals(q,contq)
        return contp==contq