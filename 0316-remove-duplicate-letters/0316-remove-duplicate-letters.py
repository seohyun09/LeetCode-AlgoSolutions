class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter={}
        seen={}
        stack=[]

        for i in range(len(s)):
            if s[i] in counter.keys():
                counter[s[i]]+=1
            else:
                counter[s[i]]=1
                seen[s[i]]=0
        
        for i in range(len(s)):
            counter[s[i]]-=1

            if seen[s[i]] and seen[s[i]]>0: continue

            while stack and stack[-1]>s[i] and counter[stack[-1]]>0:
                seen[stack.pop()]=0
            
            stack.append(s[i])
            seen[s[i]]=1
        
        return ''.join(stack)