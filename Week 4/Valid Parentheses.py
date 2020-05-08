class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
     
        stack=[]
        for par in s:
            if par == "(" or par == "[" or par == "{":
                stack.append(par)
            else:
                if par==")" and stack:
                    if stack.pop()=="(":
                        continue
                    else:
                        return False
                            
                elif par=="]" and stack:
                    if stack.pop()=="[":
                        continue
                    else:
                        return False                    
                    
                elif par=="}" and stack:
                    if stack.pop()=="{":
                        continue
                    else:
                        return False
                
                else: return False
        
        return len(stack)==0