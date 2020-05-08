class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.back(S)==self.back(T)
       
    
    def back(self,strg):
        stack = []
        for let in strg:
            if let=="#":
                if stack:
                    stack.pop()
            else: stack.append(let)
        return stack