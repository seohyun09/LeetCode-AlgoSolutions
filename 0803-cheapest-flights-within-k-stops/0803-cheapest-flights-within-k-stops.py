class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF=int(1e9)
        distance=[INF]*n
        distance[src]=0

        for i in range(k+1):
            temp=distance[:]
            for u, v, w in flights:
                if distance[u]+w<temp[v]:
                    temp[v]=distance[u]+w
            distance=temp
        
        return -1 if distance[dst]==INF else distance[dst]