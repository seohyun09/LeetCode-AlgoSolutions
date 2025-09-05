class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}
        for i in range(len(nums)):
            if nums[i] in hash_map.keys():
                hash_map[nums[i]]+=1
            else:
                hash_map[nums[i]]=1
        hash_map=sorted(hash_map.items(), key=lambda item:item[1], reverse=True)

        answer=[]
        for i in range(k):
            answer.append(hash_map[i][0])
        return answer