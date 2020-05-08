class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(left,right+1,1):
            if len(str(i))==1:
                ans.append(i)
            else:
                count = 0
                for digit in str(i):
                    if int(digit)!=0 and i%int(digit)==0:
                        count = count+1
                        if count == len(str(i)):
                            ans.append(i)
                        
        return ans