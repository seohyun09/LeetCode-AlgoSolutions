class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=[[] for _ in range (n+1)]
        visited=[False]*(n+1)
        INF=int(1e9)
        distance=[INF]*(n+1)
        S=[]

        for i in range(len(times)):
            graph[times[i][0]].append((times[i][1], times[i][2]))
        
        visited[k]=True
        distance[k]=0
        S.append(k)

        def min_node():
            min_value=INF
            idx=0
            for i in range(1, n+1):
                if not visited[i] and min_value>distance[i]:
                    min_value=distance[i]
                    idx=i
            return idx

        while len(S)<n:
            for v, w in graph[k]:
                if not visited[v]:
                    distance[v]=min(distance[v], distance[k]+w)
            
            k=min_node()
            visited[k]=True
            S.append(k)

        if max(distance[1:])!=INF:
            return max(distance[1:])
        else:
            return -1

