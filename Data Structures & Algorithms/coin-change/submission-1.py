class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        agenda = deque([(0, amount)])
        seen = set()

        while agenda:
            for _ in range(len(agenda)):
                num, amt = agenda.popleft()
                if amt == 0:
                    return num
                for coin in coins:
                    if amt - coin >= 0 and (amt - coin) not in seen:
                        agenda.append((num + 1, amt - coin))
                        seen.add(amt - coin)
        return -1
            
