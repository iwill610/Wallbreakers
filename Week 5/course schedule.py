class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        classmap = [[] for cl in range(numCourses)]
        indegree = [0 for cl in range(numCourses)]
        for cl,pre in prereq:
            classmap[pre].append(cl) #pre--->class
            indegree[cl]+=1 #how many pre for a given class
        if 0 not in indegree:
            return False
        queue = collections.deque([i for i in range(numCourses) if indegree[i]==0])
        cantake = len(queue)
        while queue:
            taken = queue.popleft() 
            for cl in classmap[taken]:
                indegree[cl]-=1
                if indegree[cl]==0:
                    cantake+=1
                    queue.append(cl)
        return numCourses==cantake