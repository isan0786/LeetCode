# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s1) > len(s2):
#             return False

#         # idx_count = { (i): 0 for i in range(26)}
#         # initializing lower case dict from a - z
#         s1Map = {chr(ord('a') + i): 0 for i in range(26)}
#         s2Map = {chr(ord('a') + i): 0 for i in range(26)}


#         for i in range(len(s1)):
#             s1Map[s1[i]] += 1
#             s2Map[s2[i]] += 1
#             # s1-2Map.get(s1-2[i]), no need to keep s1Map.get(s1-2[i],0)

#         matches = 0

#         for i in s1Map:
#             matches += 1 if (s1Map.get(i) == s2Map.get(i)) else 0
#             # s1-2Map.get(s1-2[i]), no need to keep s1Map.get(s1-2[i],0) because there will never be the case when the obj in dict does not exist because we already initialized from a-z

#         l = 0 #starting from left index
#         for r in range(len(s1), len(s2)):
#             if matches == 26: return True

#             s2Map[s2[l]] -= 1
#             s2Map[s2[r]] += 1

#             if (s2Map[s2[l]] == s1Map[s2[l]]):
#                 matches += 1
#             else:
#                 matches -= 1

#             if s2Map[s2[r]] == s1Map[s2[r]]:
#                 matches += 1  
#             else:
#                 matches -= 1
            
#             l += 1
        
#         return matches == 26
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
