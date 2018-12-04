from lcs import _lcs

def all_scs(str1, str2):
    cache = _lcs(str1, str2)

    tracks = [(len(cache)-1, len(cache[0])-1, "")]

    result = []
    while tracks:
        tracks_new = []
        for track in tracks:
            idx2, idx1, msg = track
            if idx1 == 0 and idx2 == 0:
                result.append(msg)
            else:
                if idx1 > 0 and idx2 > 0 and str1[idx1-1] == str2[idx2-1]:
                    tracks_new.append((idx2-1, idx1-1, str1[idx1-1] + msg))
                else:
                    go_up = False
                    if idx1 == 0 or (idx2 > 0 and cache[idx2-1][idx1] >= cache[idx2][idx1-1]):
                        go_up = True
                    go_left = False
                    if idx2 == 0 or (idx1 > 0 and cache[idx2][idx1-1] >= cache[idx2-1][idx1]):
                        go_left = True
                    if go_up:
                        tracks_new.append((idx2-1, idx1, str2[idx2-1] + msg))
                    if go_left:
                        tracks_new.append((idx2, idx1-1, str1[idx1-1] + msg))
        tracks = tracks_new
    return result

print(all_scs("ABCBDAB", "BDCABA"))

