class Solution:
    def findOrder(self, n: int, prereq: List[List[int]]) -> List[int]:
        classmap=[[] for cl in range(n)] #classes you can take after doing given prereq
        indegree = [0 for cl in range(n)] #num of pre for a given class
        
        for cl,pre in prereq:
            classmap[pre].append(cl)
            indegree[cl]+=1
        
        if 0 not in indegree:
            return []
        queue=collections.deque([i for i in range(n) if indegree[i]==0])
        order = [i for i in range(n) if indegree[i]==0]    
        
        while queue:
            taken = queue.popleft()
            for cl in classmap[taken]:
                indegree[cl]-=1
                if indegree[cl]==0:
                    queue.append(cl)
                    order.append(cl)
        if len(order)==n:
            return order
        else:
            return []