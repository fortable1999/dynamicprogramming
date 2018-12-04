
def solution(A):
    # write your code in Python 3.6
    subresults = [0 for x in range(len(A))]
    subresults[0] = A[0]

    for idx in range(1, len(A)):
        possible_prev = []
        if idx - 1 >= 0:
            possible_prev.append(subresults[idx - 1])
        if idx - 2 >= 0:
            possible_prev.append(subresults[idx - 2])
        if idx - 3 >= 0:
            possible_prev.append(subresults[idx - 3])
        if idx - 4 >= 0:
            possible_prev.append(subresults[idx - 4])
        if idx - 5 >= 0:
            possible_prev.append(subresults[idx - 5])
        if idx - 6 >= 0:
            possible_prev.append(subresults[idx - 6])
        subresults[idx] = max(possible_prev) + A[idx]

    return subresults[-1]

print(solution([1, -2]))

