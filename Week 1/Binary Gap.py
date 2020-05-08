class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        #create array of indicies of 1's (going from right to left of bin rep)
        A=[i for i in range(32) if (N>>i)&1]
        diff = 0
        if len(A)<2:
            return 0
        else:
            for j in range(len(A)-1):
                if A[j+1]-A[j] > diff:
                    diff = A[j+1]-A[j]
        return diff