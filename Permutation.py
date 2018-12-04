def solution(A):
    # write your code in Python 3.6

    if max(A) != len(A):
        return 0
    appear  = [1 for x in range(len(A))]

    for elem in A:
        appear[elem - 1] = 0

    if sum(appear) == 0:
        return 1
    else:
        return 0

print(solution([1,2,3,4]))
print(solution([1,2,3]))
print(solution([1,2,4]))
print(solution([1,1,1,1,4]))
print(solution([2,2,2,4]))


