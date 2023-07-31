class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for n in nums:
            if n in hashmap:
                return True
            hashmap[n] = 1
        return False

# space complexity of the dictionary is O(n) because each n elements is stored in the memory.
# time complexity of the dictionary is also O(n), the number of elements that we are iterating through are n
