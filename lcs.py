def optimized_lcs(data1, data2):
    # LCS table:
    #   D A T A 1
    # D
    # A
    # T
    # A
    # 2
    temp_data = [0 for x in range(len(data1) + 1)]
    for idx2 in range(1, len(data2) + 1):
        temp_data_next = [0 for x in range(len(data1) + 1)]
        for idx1 in range(1, len(data1) + 1):
            if data1[idx1 - 1] == data2[idx2 - 1]:
                temp_data_next[idx1] = temp_data[idx1 - 1] + 1
            else:
                temp_data_next[idx1] = max(temp_data_next[idx1 - 1], temp_data[idx1])
        temp_data = temp_data_next
    return temp_data[-1]

def _lcs(data1, data2):
    # LCS table:
    #   D A T A 1
    # D
    # A
    # T
    # A
    # 2
    temp_data = [[0] * (len(data1) + 1)]
    for idx2 in range(1, len(data2) + 1):
        temp_data_next = [0 for x in range(len(data1) + 1)]
        for idx1 in range(1, len(data1) + 1):
            if data1[idx1 - 1] == data2[idx2 - 1]:
                temp_data_next[idx1] = temp_data[idx2 - 1][idx1 - 1] + 1
            else:
                temp_data_next[idx1] = max(temp_data_next[idx1 - 1], temp_data[idx2 - 1][idx1])
        temp_data.append(temp_data_next)
    return temp_data

def all_lcs(data1, data2):
    # LCS table:
    #   D A T A 1
    # D
    # A
    # T
    # A
    # 2
    lcs_table = _lcs(data1, data2)

    # init traces: [(x, y, String), ...]
    traces = [(len(data2), len(data1), "")]
    result = []
    while traces:
        new_traces = []
        for trace in traces:
            idx2 = trace[0]
            idx1 = trace[1]
            seq = trace[2]
            if lcs_table[idx2-1][idx1-1] == 0:
                result.append(data1[idx1-1]+seq)
            elif lcs_table[idx2-1][idx1] < lcs_table[idx2][idx1] and lcs_table[idx2][idx1-1] < lcs_table[idx2][idx1]:
                new_traces.append((idx2-1, idx1-1, data1[idx1-1]+seq))
            elif lcs_table[idx2-1][idx1] < lcs_table[idx2][idx1] and lcs_table[idx2][idx1-1] == lcs_table[idx2][idx1]:
                new_traces.append((idx2, idx1-1, seq))
            elif lcs_table[idx2-1][idx1] == lcs_table[idx2][idx1] and lcs_table[idx2][idx1-1] < lcs_table[idx2][idx1]:
                new_traces.append((idx2-1, idx1, seq))
            else:
                new_traces.append((idx2-1, idx1, seq))
                new_traces.append((idx2, idx1-1, seq))
        traces = new_traces
    return result



# print(_lcs("AGGTAB", "GXTXAYB"))
# print(optimized_lcs("AGGTAB", "GXTXAYB"))
# print(all_lcs("ABCBDAB", "BDCABA"))
