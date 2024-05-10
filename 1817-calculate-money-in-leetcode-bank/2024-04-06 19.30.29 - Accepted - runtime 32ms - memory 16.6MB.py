class Solution:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        money = w * 28
        money += (7 * w *( w - 1))//2

        if (n % 7):
            extra_days = n % 7
            money_to_add = w + 1
            for i in range(extra_days):
                money += money_to_add
                money_to_add += 1

        return money