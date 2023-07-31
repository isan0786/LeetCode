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

# code time complexity is O(m*n*26) = O(m*n)
# space complexity -> O(n)
'''
res: This is a dictionary (defaultdict) that stores the anagrams grouped by their character counts. The space required for this dictionary depends on the number of unique character count patterns found in the input list strs. In the worst case, each string in strs is an anagram of a different pattern, leading to all n strings being stored separately. In this case, the space complexity of res would be O(n).

count: This is a list of 26 integers used to count the occurrences of each character in a string. It is created and updated for each string in strs. Since the size of count is fixed (26 elements) and independent of the input size, its space complexity is constant, O(1).
'''
