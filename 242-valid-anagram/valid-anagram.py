class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False

        return True

# The space complexity is O(n) because the dictionary requires space of n elements in the memory
# the time complexity is O(n) because the dictionary has n elements in it, and the search from each element is O(1)
