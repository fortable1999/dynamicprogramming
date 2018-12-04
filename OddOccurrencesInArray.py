def solution(A):
    # write your code in Python 3.6
    sort_a = sorted(A)
    idx = 0
    while True:
        if idx + 1 >= len(sort_a):
            return sort_a[idx]
        else:
            if sort_a[idx] != sort_a[idx + 1]:
                return sort_a[idx]
            else:
                idx += 2

print(solution([100000002] + [x for x in range(2, 1000000)] * 2))



