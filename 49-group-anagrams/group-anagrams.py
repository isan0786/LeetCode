class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the reason for this defaultdict function is because we are trying to acces the initial values for key's at line 11 which does not even exist initially, so dealing with that error we have to use the defaultdict, which will just return the empty [] list for the key that does not exist
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # create an empty list with 26 elements all filled with 0's
            for char in s:
                count[ord(char)-ord("a")] += 1
            
            # becuase we can't store key as a list because it's mutable so, we have to store tuple which is immutable.
            res[tuple(count)].append(s)

        return res.values()
