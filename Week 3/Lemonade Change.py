class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if bills[0]>5:
            return False
        fives = 0
        tens = 0
        for amt in bills:
            if amt ==5:
                fives+=1
            elif amt ==10:
                fives-=1
                tens+=1
            else: 
                if tens>=1 and fives>=1:
                    tens-=1
                    fives-=1
                    
                else:
                    fives-=3
                    
            if fives<0 or tens<0:
                return False
            
        return True