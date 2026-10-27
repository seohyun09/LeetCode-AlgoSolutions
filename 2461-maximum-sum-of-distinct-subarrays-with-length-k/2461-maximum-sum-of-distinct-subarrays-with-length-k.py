class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        
        n = len(nums)
        start, end = 0, k

        hash_map = {}
        total, answer = 0, 0

        for i in range(start, end):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 0
            hash_map[nums[i]] += 1

            total += nums[i]
        
        if len(hash_map) == k:
            answer = total

        while end < n:
            
            hash_map[nums[start]] -= 1
            total -= nums[start]
            
            if hash_map[nums[start]] == 0:
                del hash_map[nums[start]]

            start += 1

            if nums[end] not in hash_map:
                hash_map[nums[end]] = 0
            hash_map[nums[end]] += 1
            total += nums[end]

            end += 1

            if len(hash_map) == k:
                answer = max(answer, total)

        return answer