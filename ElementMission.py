def solution(A):
    # write your code in Python 3.6
    sort_a = sorted(A)
    result = len(sort_a) + 1
    for idx in range(len(sort_a)):
        if sort_a[idx] != (idx + 1):
            return idx + 1
    return result

print(solution([1,2,3,5]))
print(solution([]))
print(solution([2]))
print(solution([x for x in range(1000000, 0, -1)]))
