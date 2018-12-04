def optimized_lrs(data):
    cache = [0] * (len(data) + 1)

    for idx2 in range(1, len(data) + 1):
        new_cache = [0] * (len(data) + 1)
        for idx1 in range(1, len(data) + 1):
            if data[idx1-1] == data[idx2-1] and idx1 != idx2:
                new_cache[idx1] = cache[idx1-1] + 1
            else:
                new_cache[idx1] = max(cache[idx1], new_cache[idx1-1])
        cache = new_cache
    return cache

def _lrs(data):
    cache = [[0] * (len(data) + 1)]

    for idx2 in range(1, len(data) + 1):
        new_cache = [0] * (len(data) + 1)
        for idx1 in range(1, len(data) + 1):
            if data[idx1-1] == data[idx2-1] and idx1 != idx2:
                new_cache[idx1] = cache[idx2-1][idx1-1] + 1
            else:
                new_cache[idx1] = max(cache[idx2-1][idx1], new_cache[idx1-1])
        cache.append(new_cache)
    return cache

print(optimized_lrs("ATACTCGGA"))
print(_lrs("ATACTCGGA"))

                

