from typing import List
import random

# Not an original answer, guidance taken from YouTube

class Solution:
    """
    You are given coins of different denominations and a total amount of money.
    Write a function to compute the number of combinations that make up that amount.
    You may assume that you have infinite number of each kind of coin.
    """
    # the number of ways to make 5 from [1, 2, 5] =
    #   the number of ways to make 5 by using the last coin             change(0, [1, 2, 5])
    #   + the number of ways to make 5 without using the last coin      change(5, [1, 2])

    def change(self, amount: int, coins: List[int]) -> int:
        self.memo = {}
        return self.change_coins(amount, coins, len(coins))

    def change_coins(self, amount, coins, max_index):
        if amount == 0:
            return 1
        elif (amount, max_index) in self.memo:
            return self.memo[(amount, max_index)]
        elif amount < 0 or max_index == 0:
            return 0

        with_last_coin = self.change_coins(amount - coins[max_index - 1], coins, max_index)
        without_last_coin = self.change_coins(amount, coins, max_index - 1)
        number_of_times = with_last_coin + without_last_coin
        self.memo[(amount, max_index)] = number_of_times
        return number_of_times


amt = 500
coins = [1,2, 5]
# random.shuffle(coins)

result = Solution().change(amt, coins)
print(result)
