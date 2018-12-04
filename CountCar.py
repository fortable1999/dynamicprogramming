def solution(A):
    # write your code in Python 3.6
    counts = [0 for x in range(len(A))]
    zeros = [0 for x in range(len(A))]
    sum_1 = 0
    for idx in range(len(A)-1, -1, -1):
        if A[idx] == 1:
            counts[idx] = sum_1
            sum_1 += 1
        else:
            counts[idx] = sum_1
            zeros[idx] = 1
    result = 0
    for idx, elem in enumerate(zeros):
        if elem == 1:
            result += counts[idx]
            if result > 1000000000:
                return -1
    return result

print(solution([1]))

