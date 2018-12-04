def mxis(data):
    sums = [0] * len(data)

    for idx in range(len(data)):
        if idx == 0:
            sums[idx] = data[idx]
            continue
        max_sub = sums[0]
        for idx_sub in range(idx):
            if data[idx] > data[idx_sub]:
                max_sub = max(sums[idx_sub] + data[idx], max_sub)
        sums[idx] = max_sub
    return sums

print(mxis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))


