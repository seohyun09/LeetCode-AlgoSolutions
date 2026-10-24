import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        
        INF = float('inf')

        n = len(heights)
        m = len(heights[0])

        # 상, 하, 좌, 우
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]

        def dijkstra(si, sj):
            
            visited = [[False] * m for _ in range(n)]

            effort = [[INF] * m for _ in range(n)]
            effort[0][0] = 0

            pq = []
            heapq.heappush(pq, (0, si, sj))

            while pq:
                w, i, j = heapq.heappop(pq)

                if visited[i][j]:
                    continue

                visited[i][j] = True

                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]

                    if ni < 0 or ni >= n or nj < 0 or nj >= m:
                        continue
                    
                    new_effort = max(w, abs(heights[i][j] - heights[ni][nj]))

                    if not visited[ni][nj] and new_effort < effort[ni][nj]:
                        effort[ni][nj] = new_effort
                        heapq.heappush(pq, (new_effort, ni, nj))
                        
            return effort[n-1][m-1]

        return dijkstra(0, 0)