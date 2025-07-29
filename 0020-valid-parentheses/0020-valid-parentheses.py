class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map={'{':'}', '[':']', '(':')'}
        stack1, stack2=[], []
        for i in range(len(s)):
            stack1.append(s[i])

        while stack1:
            parentheses=stack1.pop()
            if parentheses in parentheses_map.values():
                stack2.append(parentheses)
            elif parentheses in parentheses_map.keys():
                if stack2 and parentheses_map[parentheses]==stack2[-1]:
                    stack2.pop()
                else:
                    return False
        if stack2: return False
        
        return True
            

        