from queue import PriorityQueue

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        que=PriorityQueue()
        for i in range(len(points)):
            distance=sqrt(points[i][0]**2+points[i][1]**2)
            que.put((distance, points[i]))
        answer=[]
        for _ in range(k):
            answer.append(que.get()[1])
        return answer