def solution(s):
    numbers = s.split()

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    minimum = min(numbers)
    maximum = max(numbers)

    answer = str(minimum) + " " + str(maximum)
    return answer