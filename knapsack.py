def knapsack(weights, values, max_weight):
    cache = [0] * (max_weight + 1)
    for item_idx in range(len(weights)):
        new_cache = [0] * (max_weight + 1)
        for weight in range(1, max_weight + 1):
            if weights[item_idx] > weight:
                new_cache[weight] = cache[weight]
            else:
                new_cache[weight] = max(cache[weight], values[item_idx] + cache[weight - weights[item_idx]])
        cache = new_cache
    return cache[-1]

print(knapsack([1,2,3,8,7,4], [20, 5, 10, 40, 15, 25], 10))
