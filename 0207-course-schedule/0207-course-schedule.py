from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue=deque()
        in_degree={i: 0 for i in range(numCourses)}
        visited=[False]*numCourses
        T=[]
        graph={}

        if len(prerequisites)==1 or len(prerequisites)==0:
            return True

        for i in range(len(prerequisites)):
            if prerequisites[i][0] in in_degree.keys():
                in_degree[prerequisites[i][0]]+=1
            else:
                in_degree[prerequisites[i][0]]=1
            
            if prerequisites[i][1] in graph.keys():
                graph[prerequisites[i][1]].append(prerequisites[i][0])
            else:
                graph[prerequisites[i][1]]=[prerequisites[i][0]]

        for u in in_degree:
            if in_degree[u]==0:
                queue.append(u)
                visited[u]=True

        while queue:
            v=queue.popleft()
            T.append(v)

            for neighbor in graph.get(v, []):
                in_degree[neighbor]-=1
                if in_degree[neighbor]==0:
                    queue.append(neighbor)
                    visited[neighbor]=True
        
        if len(T)==numCourses:
            return True
        else:
            return False     
