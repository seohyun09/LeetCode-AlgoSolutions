import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        
        INF = float('inf')

        # 인접 리스트
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((w, v))

        
        def dijkstra(node):
            
            visited = [False] * (n + 1)
            dist = [INF] * (n + 1)
            dist[node] = 0
            dist[0] = 0
            visited[node] = True

            pq = []
            heapq.heappush(pq, (0, node))

            while pq:
                w, curr = heapq.heappop(pq)

                visited[curr] = True

                for weight, nxt in graph[curr]:
                    new_dist = dist[curr] + weight
                    
                    if not visited[nxt] and new_dist < dist[nxt]:
                        dist[nxt] = new_dist
                        heapq.heappush(pq, (new_dist, nxt))
            
            answer = 0
            for i in range(1, n + 1):
                answer = max(answer, dist[i])
            
            if answer == INF:
                return -1
            
            return answer

        return dijkstra(k)