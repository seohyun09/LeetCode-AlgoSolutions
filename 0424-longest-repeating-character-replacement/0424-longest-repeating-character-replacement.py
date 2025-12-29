class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        left, right = 0, 0
        answer = 0
        while right < len(s):
            if s[right] not in hash_map:
                hash_map[s[right]] = 1
            else:
                hash_map[s[right]] += 1
            maxCount = max(hash_map.values())

            if right - left - maxCount + 1 > k:
                hash_map[s[left]] -= 1
                left += 1
            
            
            right += 1
    
        return len(s) - left
