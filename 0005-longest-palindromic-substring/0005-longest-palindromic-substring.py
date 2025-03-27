class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findPalindrome(left, right, s):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1

            return s[left+1:right]
            
        palindrome=''
        
        for i in range(len(s)):
            odd=findPalindrome(i, i, s)
            if len(palindrome)<len(odd):
                palindrome=odd

            even=findPalindrome(i, i+1, s)
            if len(palindrome)<len(even):
                palindrome=even
        
        return palindrome

        
