def solution(s):
    numbers = s.split()

    minimum = int(numbers[0])
    maximum = int(numbers[0])

    for num in numbers:
        num = int(num)

        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

    return str(minimum) + ' ' + str(maximum)