# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


# Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #We are using the 2 pointer approach in this 

        L = 0 # Buying Price
        R = 0 # Selling Price
        maxProfit = 0 


        while R < len(prices): # Setting condition for the right pointer
            if prices[L] < prices[R]: # we want buying price to be less than selling price
                profit = prices[R] - prices[L] # simple math calculating profit
                maxProfit = max(maxProfit, profit) # comparing with the maxProfit till now and updating maxProfit based on profit
            else:
                L = R # moving L pointer to r as we got the next least price 
            R += 1 #need to increment pointer to move to the next case

        return maxProfit # returning the maxProfit
