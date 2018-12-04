from lcs import _lcs

def diff(str1, str2):
    cache = _lcs(str1, str2)

    idx2, idx1, msg = len(cache)-1, len(cache[0])-1, ""

    while idx2 > 0 or idx1 > 0:
        if str1[idx1-1] == str2[idx2-1] and idx1 > 0 and idx2 > 0:
            msg = str1[idx1-1] + msg
            idx2 -= 1
            idx1 -= 1
        elif idx1 > 0 and (idx2 == 0 or cache[idx2][idx1-1] >= cache[idx2-1][idx1]):
            msg = "(-" + str1[idx1-1] + ")" + msg
            idx1 -= 1
        elif idx2 > 0 and (idx1 == 0 or cache[idx2-1][idx1] >= cache[idx2][idx1-1]):
            msg = "(+" + str2[idx2-1] + ")" + msg
            idx2 -= 1
    return msg

print(diff("ABABC", "BABCA"))
