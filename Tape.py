import math
def solution(A):
    # write your code in Python 3.6
    left, right = A[0], sum(A[1:])
    diff = abs(left - right)

    for elem in A[1:-1]:
        left += elem
        right -= elem
        if abs(left - right) < diff:
            diff = abs(left - right)

    return diff

print(solution([-1, 1, 1000, -1]))
print(solution([1, -1, -11]))
print(solution([1, 2]))
