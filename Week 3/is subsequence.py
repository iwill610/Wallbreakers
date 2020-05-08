class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ##attempt 3
        sub=len(s)
        seq=len(t)
        if sub>seq:
            return False
        if sub==0:
            return True
        check=''
        u=0
        e=0
        while u<sub and e<seq:
            if s[u]!=t[e]:
                
                e+=1
            else:
                check+=t[e]
                u+=1
                e+=1
        return check==s
        
        ##attempt 2 **works**
#         t = iter(t)
        
#         return all(i in t for i in s)
        
        ##attempt 1
        
#         check = []
#         for letter in s:
#             if t.find(letter)>-1:
#                 check.append(t.rfind(letter))
#                 print(check)
#             else:
#                 return False
#         for i in check:
#             i=int(i)
        
        
                
#         return  check==sorted(check)