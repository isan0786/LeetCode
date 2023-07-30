class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # or for i, n in enumerate(nums)
        for i in range(len(nums)):
            diff = (target - nums[i])
            if diff in hashmap:
                return [i,hashmap.get(diff)]
            hashmap[nums[i]] = i

# complexity = Space -> O(n) because elements are getting stored in the hashmap one by one using for loop
# time -> O(n) because of the for loop