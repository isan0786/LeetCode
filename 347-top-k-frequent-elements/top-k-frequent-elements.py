class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         
         #this algorithm uses bucket sort
         
         count = {}
         freq = [ [] for i in range(len(nums)+1)]

         for num in nums:
             count[num] = 1 + count.get(num,0)
        
         for n,c in count.items():
             freq[c].append(n)


         res = []

         # this will not access the element at freq[0] because of range(len(freq)-1,0,-1). and it does not matter for us what's at index 0 anyways. index 0 means element occured 0 times which will never be the case.
#  we are accessing the elements from behind this means the top big element occuremence will always start from behind
         for i in range(len(freq)-1,0,-1):

             for n in freq[i]:
                 res.append(n) 
                    # it's 2 because we always require top 2 frequently occured numbers
                 if len(res) == k:
                     return res


# time complexity O(n)
# space complexity O(n)
