class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        new=[]
        
        if len(intervals)<=1:
            return intervals
        merge1=intervals[0][0]
        merge2=intervals[0][1]
        
        new.append([merge1,merge2])
        for bgn,end in intervals[1::]:
            if bgn>new[-1][1]:
                new.append([bgn,end])
                merge1=bgn
                merge2=end
            else:
                new[-1][1]=max(merge2,end)
                merge2=new[-1][1]
                
        return new