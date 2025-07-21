class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins = sorted(coins)
        memo = {}
        return self.helper(coins, amount, memo)

    def helper(self, coins, amount, memo):
        if amount == 0:
            return 0

        if amount in memo:
            return memo[amount]
        min_subres = float("inf")
        for coin in coins:
            if coin > amount:
                break
            sub_res = self.helper(coins, amount - coin, memo)
            if sub_res != -1:
                min_subres = min(min_subres, sub_res)
        
        res = -1 if min_subres == float("inf") else min_subres + 1
        memo[amount] = res
        return res
