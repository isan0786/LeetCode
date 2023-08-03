class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The output array does not count as extra space for space complexity analysis. (according to the question). But technically, it does take the O(n) space
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix*=nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix *= nums[i]

        return res


        # this has a space complexity of O(1, due to line #4) and time complexity of O(n)