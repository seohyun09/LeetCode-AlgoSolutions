from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1: return [0]
        if n==2: return edges[0]

        in_degree=[0]*n
        graph={i: [] for i in range(n)}
        for i in range(len(edges)):
            in_degree[edges[i][0]]+=1
            in_degree[edges[i][1]]+=1
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])

        que=deque()
        for i in range(n):
            if in_degree[i]==1:
                que.append(i)
        
        remaining=n
        while remaining>2:
            size=len(que)
            remaining-=size
            for i in range(size):
                node=que.popleft()
                for u in graph[node]:
                    in_degree[u]-=1
                    if in_degree[u]==1:
                        que.append(u)

        return list(que)