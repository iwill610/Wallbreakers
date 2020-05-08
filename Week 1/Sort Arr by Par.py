class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        b=[]
        for i in A:
            if i%2==0:
                b.insert(0,i)
            else:
                b.append(i)
        return b