def optimized_substring(str1, str2):
    cache = [0] * (len(str1) + 1)
    max_length = 0

    for idx2 in range(1, len(str2)+1):
        new_cache = [0] * (len(str1) + 1)
        for idx1 in range(1, len(str2)+1):
            if str1[idx1-1] == str2[idx2-1]:
                new_cache[idx1] = cache[idx1-1] + 1
                if new_cache[idx1] > max_length:
                    max_length = new_cache[idx1]
        cache = new_cache
    return max_length

def _substring(str1, str2):
    cache = [[0] * (len(str1) + 1)]
    max_length = 0

    for idx2 in range(1, len(str2)+1):
        new_cache = [0] * (len(str1) + 1)
        for idx1 in range(1, len(str2)+1):
            if str1[idx1-1] == str2[idx2-1]:
                new_cache[idx1] = cache[idx2-1][idx1-1] + 1
                if new_cache[idx1] > max_length:
                    max_length = new_cache[idx1]
        cache.append(new_cache)
    return max_length, cache

def all_substrings(str1, str2):
    max_length, cache = _substring(str1, str2)
    result = []

    for idx2 in range(len(cache)):
        for idx1 in range(len(cache[0])):
            if cache[idx2][idx1] == max_length:
                result.append("".join([str1[idx1-i] for i in range(max_length, 0, -1)]))
    return result


print(optimized_substring("ABABC", "BABCA"))
print(all_substrings("ABABC", "BABCA"))

