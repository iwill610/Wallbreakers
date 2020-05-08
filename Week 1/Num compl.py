class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
    
        x=bin(num)[2::]
        x=[str(i) for i in x]
        
        for i in range(len(x)):
            if x[i]=='0':
                x[i]='1'
            else:
                x[i]='0'
        
        return int(''.join(x),2)