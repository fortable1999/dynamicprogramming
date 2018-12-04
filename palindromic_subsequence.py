from lcs import optimized_lcs, all_lcs

def palindromic(seq):
    reversed_seq = "".join(reversed(seq.split()))
    return optimized_lcs(seq, reversed_seq)

def all_palindromic(seq):
    reversed_seq = "".join(reversed(seq))
    return all_lcs(seq, reversed_seq)

print(all_palindromic("ABBDCACD"))
