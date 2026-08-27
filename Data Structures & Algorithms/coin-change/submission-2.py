class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            out = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    out = min(out, 1 + dfs(amount - coin))
            memo[amount] = out
            return out
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins
