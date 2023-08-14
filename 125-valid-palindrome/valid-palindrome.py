class Solution:
    def sol1(self, s: str) -> bool:
        newStr = ''

        for i in s:
            if i.isalnum():
                newStr += i.lower() 
        
        # this solution takes extra memory when we create a var, newStr and also when newStr[::-1] is used.
        # this has a time complexity of O(n) and space O(n)
        return newStr == newStr[::-1] 



    ################ sol 2@@@@@@@@@@@@@@@@@@@@@@@
    def alphaNum(self,c):
        return      (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        l, r = 0,len(s)-1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1

            while r > l and not self.alphaNum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l,r = l+1, r-1
        return True

        # this solution does not takes any extra memory because there are no new string created. So, Space is O(1) and time is O(N)

    
