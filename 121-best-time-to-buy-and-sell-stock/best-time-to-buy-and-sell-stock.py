class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l is buy, r is sell
        l,r = 0,1
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                maxProfit=max(prices[r]-prices[l],maxProfit)
            
            else:
                l = r

            r += 1

        return maxProfit

        # time - O (N) and Space - O(1)