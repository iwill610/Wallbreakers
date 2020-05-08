class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)==0:
            return 0
        # if len(points)==1:
        #     return 1
        points.sort(reverse=True)
        lb = points[0][0]
        
        answer=1
        
        for lower,upper in points:
            if upper<lb:
                answer+=1
                lb=lower
                  
        return answer