"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ###iterative
        if not root:
            return []
        ans=[]
        stack=[root]
        while stack:
            current=stack.pop()
            ans+=[current.val]
            for child in current.children:
                stack.append(child)
        return ans[::-1]
        
        ###recursive
        ans=[]
        if not root:
            return []
        
        for child in root.children:
            ans+=self.postorder(child)
        ans.append(root.val)
        return ans