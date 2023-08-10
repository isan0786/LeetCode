class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(","}":"{","]":"["}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1]==closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        
        # time complexity = O(n) and 
        # space complexity = O(n) becuase all the values are getting stored in a stack + O(3) for dictionary