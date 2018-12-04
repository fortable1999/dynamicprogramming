def solution(X, Y, D):
    # write your code in Python 3.6
    result = int((Y - X) / D)

    if X + result * D < Y:
        result += 1
    return result

print(solution(8500000, 8500000, 30))
