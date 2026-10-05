# считает количество способов набрать сумму монетами
def count_change_ways(amount: int, coins: list) -> int:
    coins = sorted(set(coins))
    ways = [0] * (amount + 1)
    ways[0] = 1

    for coin in coins:
        for current_amount in range(coin, amount + 1):
            ways[current_amount] += ways[current_amount - coin]

    return ways[amount]


if __name__ == "__main__":
    amount = 5
    coins = [1, 2, 5]

    print("Сумма:", amount)
    print("Монеты:", coins)
    print("Количество способов:", count_change_ways(amount, coins))


# Для суммы 5 сначала получаем [1, 1, 1, 1, 1].
# Так как 1 + 1 = 2, получаем ещё [2, 1, 1, 1] и [2, 2, 1].
# Монета 5 даёт последний вариант [5].
