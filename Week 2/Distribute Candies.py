class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)),len(candies)/2)
        
        ###Attempt 3 **works**
#         sis=['x']*(len(candies)/2)
#         ans=[]
#         s = set(candies)
#         s =[i for i in s]
        
#         if len(sis)<len(s):
#             for i in range(len(sis)):
#                 sis.insert(i,s[i])
           
#         else:
#             for i in range(len(s)):
#                 sis.insert(i,s[i])
        
#         for can in range(len(sis)):
#                 if sis[can]!='x':
#                     ans.append(sis[can])    
#         return len(ans)
        
        
        
        
        ###Attempt 2
#         hmget=len(candies)/2
#         get=0
#         sis=0
#         dub =[]
#         s = set(candies)
#         for i in s:
#             if candies.count(i)>2:
#                 get+=1
#                 dub.append(i)
#             else:
                
#         if len(dub)==len(s):
#             return get
        
        
        ###Attempt 1
        # s = set(candies)
        # if len(candies)<3:
        #     return 1
        # if len(s)<3:
        #     return len(s)
        # uneven = 0
        # for i in s:
        #     if candies.count(i)>2:
        #         uneven+=1
        #     if candies.count(i)<2:
        #         uneven+=0.5
        # return int(len(set(candies))-uneven)