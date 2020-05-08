class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        
        satisfied = 0
        
        for child in g:
            for cookie in s:
                if cookie>=child:
                    satisfied+=1
                    s.remove(cookie)
                    break
                            
           
        return satisfied