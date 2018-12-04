def solution(X, A):
    # write your code in Python 3.6
    positions = [0 for x in range(X)]
    ready_to_go = X

    for time, a in enumerate(A):
        if positions[a-1] == 0:
            positions[a-1] = 1
            ready_to_go -= 1

            if ready_to_go == 0:
                return time
    else:
        return -1

print(solution(2, [1,1]))

