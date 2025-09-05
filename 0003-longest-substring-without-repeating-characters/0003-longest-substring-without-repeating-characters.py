class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        
        left, right=0, 1
        length=1
        max_length=1
        hash_map={}
        hash_map[s[left]]=1

        while right<len(s):
            if s[right] in hash_map.keys():
                while s[left]!=s[right]:
                    del hash_map[s[left]]
                    left+=1
                    length-=1
                left+=1
                length-=1
            hash_map[s[right]]=1
            right+=1
            length+=1

            if max_length<length:
                max_length=length
        
        return max_length