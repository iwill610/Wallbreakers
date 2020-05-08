class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        
        for i in range(len(ops)):
            if ops[i]=="D":
                if ops[i-1]:
                    x=stack.pop()
                    stack.append(x)
                    stack.append(x*2)
                continue
            if ops[i]=="C":
                if ops[i-1]:
                    stack.pop()
                continue
            if ops[i]=="+":
                if ops[i-1]:
                    x=stack.pop()
                    y=stack.pop()
                    stack.append(y)
                    stack.append(x)
                    stack.append(x+y)
                continue
            stack.append(int(ops[i]))
            continue
        
        return sum(stack)