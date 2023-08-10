class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest = 0

        for num in nums:
            # to check if it's a start of a sequence
            if num-1 not in numSet:
                length = 0
                while (num+length) in numSet:  # this operation to check has O(1) complexity because searching in a set takes O(1)
                    length += 1
                longest=max(longest,length)
        return longest

        # Time complexity = O(n) where n is the length of numss
        # space complexity = O(n) where n is the length of numss