class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        a=A.split()
        b=B.split()
        # howmanya = [0]*len(a)
        # howmanyb = [0]*len(b)
        # # setacheckb=set(b)
        # # setbchecka=set(a)
        # seta=set()
        # setb=set()
        
        
        ###Attempt 3
        
        c = a+b
        howmanyc = [0]*len(c)
        for word in range(len(c)):
            howmanyc[word]=c.count(c[word])
        
        newc = [c[word] for word in range(len(c)) if howmanyc[word]==1]
        return newc
    
    
        #Attempt 2
#         for word in range(len(a)):
#             howmanya[word]=a.count(a[word])
        
#         for word in range(len(b)):
#             howmanyb[word]=b.count(b[word])
        
#         newa = [a[word] for word in range(len(a)) if howmanya[word]==1]
        
#         newb = [b[word] for word in range(len(b)) if howmanyb[word]==1]
        
#         setacheckb=set(newb)
#         setbchecka=set(newa)
#         return setacheckb
#         for word in newa:
#             if word in setacheckb:
#                 continue
#             else:
#                 seta.add(word)
#         for word in newb:
#             if word in setbchecka:
#                 continue
#             else:
#                 setb.add(word)
           
#         return seta
        
        ###Attempt 1
#         for word in a:
#             if word in seta:
#                 seta.remove(word)
#             else:
#                 if word in setacheckb:
#                     continue
#                 else:
#                     seta.add(word)
#         for word in b:
#             if word in setb:
#                 setb.remove(word)
#             else:
#                 if word in setbchecka:
#                     continue
#                 else:
#                     setb.add(word)
           
#         return seta.union(setb)