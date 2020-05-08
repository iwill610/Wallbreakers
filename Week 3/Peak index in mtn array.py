class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        guess=(len(A)-1)//2
        while 0<=guess and guess<=(len(A)-1):
           
            if A[guess]>A[guess-1] and A[guess]>A[guess+1]:
                return guess
            elif A[guess]<A[guess-1]:
                guess-=1
            else:
                guess+=1