class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_map={}
        answer=0
        for i in range(len(stones)):
            if stones[i] in hash_map.keys():
                hash_map[stones[i]]+=1
            else:
                hash_map[stones[i]]=1
        
        for i in range(len(jewels)):
            if jewels[i] in hash_map.keys():
                answer+=hash_map[jewels[i]]
        
        return answer