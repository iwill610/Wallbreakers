class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        ###Attempt 3
        groups = 0 
        students = set()
        for row in range(len(M)):
            if row not in students:
                groups+=1
                self.friends(row,M,students)
        return groups
    
    def friends(self,row,M,students):
        for row,col in enumerate(M[row]):
            if col and row not in students:
                students.add(row)
                self.friends(row,M,students)
                
                
    ###Attempt 2
#         groups=0
#         students=set()
#         for row in range(len(M)):
#             if row not in students:
#                 groups+=1
                
#                 for row,col in enumerate((M[row])):
#                     if row and col not in students:
#                         #if M[row][col]==1:
#                         students.add(row)
                        
#                         #else:
#                             #continue
#             #students.add(row)
                   
                           
#         return groups

###Attempt 1?????
#         x=[]
#         g=0
#         all1=0
#         for row in range(len(M)):
#             for col in range(len(M[row])):
#                 if M[row][col]==1:
#                     all1+=1
#                     continue
#         if len(M)**2 == all1:
#             return 1
                    
            
        
#         for row in range(len(M)):
#             xrow=[]
#             for col in range(len(M[row])):
#                 if M[row][col]==1:
#                     xrow.append(col)
#             x.append(xrow)
        
#         for i in range(len(x)):
#             if len(x[i])==1:
#                 g+=1
        
        
#         ans = [] 
#         for row in range(len(x)):
#             #ansrow=[]
#             for col in range(len(x[row])):
#                 if x[row][col]>row:
#                     ans.append(x[row][col])
        
        
        
#         if len(ans)==1:
#             return len(M)-1
#         if len(ans)==0:
#             return len(M)
       
#         for i in range(len(ans)):
#             for j in range(i,len(ans)):
#                 if ans[j]-ans[i]==1 or ans[i]-ans[j]==1:
#                     break
#             else:
#                 g+=1
#         if g ==0:
#              g=1
#         return g
