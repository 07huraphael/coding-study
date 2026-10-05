def solution(s):
    numbers = list(map(int, s.split()))

    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return f"{minimum} {maximum}"