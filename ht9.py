import timeit

def implementation_time(func, total_amount, coins):
    start_time = timeit.default_timer()
    result = func(total_amount, coins)
    execution_time = timeit.default_timer() - start_time
    return result, execution_time

def find_coins_greedy(total_amount, coins):
    result = {}

    for coin in coins:

        if coin<= total_amount:
            coins_num = total_amount // coin
            result[coin] = coins_num
            total_amount -= coin*coins_num
    
    return result

def find_min_coins(total_amount, coins):
    result = {}
    n=len(coins)
    K = [[float('inf') for _ in range(total_amount + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        K[i][0] = 0

    for i in range(1, n+1):
        for amounts in range(1, total_amount+1):
            if coins[i - 1] <= amounts:
                K[i][amounts] = min(K[i - 1][amounts], 1 + K[i][amounts - coins[i - 1]])
            else:
                K[i][amounts] = K[i - 1][amounts]

    amount = total_amount
    for i in range(n, 0, -1):
        while amount >= coins[i - 1] and K[i][amount] == 1 + K[i][amount - coins[i - 1]]:
            coin = coins[i - 1]
            result[coin] = result.get(coin, 0) + 1
            amount -= coin
    return result
   
coins = [50, 25, 10, 5, 2, 1]
total_amounts = [113, 2312, 23134, 234563, 9987431]
functions = [find_coins_greedy, find_min_coins]

for total_amount in total_amounts:
    for function in functions:
        result, execution_time = implementation_time(function, total_amount, coins)
        print(f"Для суми {total_amount}: Алгоритм: {function.__name__}; Результат: {result}; Час виконання: {execution_time:.6f}")