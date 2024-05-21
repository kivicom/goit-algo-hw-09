def find_coins_greedy(amount):
    '''Функція жадібного алгоритму:'''
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
        amount %= coin

    return result

# Приклад використання
print(find_coins_greedy(113))  # {50: 2, 10: 1, 2: 1, 1: 1}


def find_min_coins(amount):
    '''Функція динамічного програмування'''
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    if dp[amount] == float('inf'):
        return {}

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Приклад використання
print(find_min_coins(113))  # {1: 1, 2: 1, 10: 1, 50: 2}
