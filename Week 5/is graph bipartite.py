class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        groupmap={}
        for node in range(len(graph)):
            if node not in groupmap:
                queue=collections.deque([node])
                groupmap[node]=0
                while queue:
                    checknode = queue.popleft()
                    for neibor in graph[checknode]:
                        if neibor not in groupmap:
                            groupmap[neibor]=1-groupmap[checknode]
                            queue.append(neibor)
                        elif groupmap[checknode]==groupmap[neibor]:
                            return False
        return True