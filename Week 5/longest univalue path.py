# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans=0
        def check(node,val):
            if not node: return 0
            if node.left:
                left=check(node.left,node.val)
            else: 
                left= 0
            if node.right:
                right=check(node.right,node.val)
            else: 
                right= 0
            self.ans=max(self.ans,right+left)
            if node.val == val:
                return 1+max(left,right)
            else:
                return 0
        
                
        
            
        check(root,root.val)
        return self.ans