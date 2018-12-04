def lis(data):
    ways = [0] * len(data)
    for idx in range(len(data)):
        if idx == 0:
            ways[idx] = 1
            continue
        max_length = 1
        for idx_sub in range(idx):
            if data[idx] > data[idx_sub]:
                max_length = max(max_length, ways[idx_sub]+1)
        ways[idx] = max_length
    return max(ways)

def lds(data):
    ways = [0] * len(data)
    for idx in range(len(data)):
        if idx == 0:
            ways[idx] = 1
            continue
        max_length = 1
        for idx_sub in range(idx):
            if data[idx] < data[idx_sub]:
                max_length = max(max_length, ways[idx_sub]+1)
        ways[idx] = max_length
    return max(ways)

print(lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
print(lds([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))

