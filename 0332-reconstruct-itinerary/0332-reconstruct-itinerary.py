from queue import PriorityQueue

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        hash_map={}
        answer=[]
        for i in range(len(tickets)):
            if tickets[i][0] not in hash_map.keys():
                hash_map[tickets[i][0]]=PriorityQueue()
            hash_map[tickets[i][0]].put(tickets[i][1])
        
        def dfs(travel):
            while travel in hash_map.keys() and not hash_map[travel].empty():
                dfs(hash_map[travel].get())
            answer.append(travel)
        
        dfs("JFK")
        return answer[::-1]