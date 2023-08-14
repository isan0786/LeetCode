class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,a in enumerate(nums):
           
            if i > 0 and a == nums[i-1]:
               continue

            l,r = i+1, len(nums)-1

            while l  < r:

                threesum = a + nums[l] + nums[r]
                if threesum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif threesum < 0:
                    l += 1
                else:
                    r -= 1
                
                
        return res
# this has a time complexity of O(nlogn (for sorting) + n^2 ), so overall it's n^2
# space complexity could be O(n) or O(1) because some sort func require space to sort the numbers in a list but some don't